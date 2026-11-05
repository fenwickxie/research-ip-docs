"""Offline scalar sequence-discrimination demo; never sends robot commands."""

import argparse
import json
import unittest
from fractions import Fraction
from itertools import combinations, product


Interval = tuple[Fraction, Fraction]
Signature = tuple[bool, ...]


def validate_sequence(sequence: tuple[Fraction, ...], bound: Fraction) -> None:
    if not sequence or bound < 0:
        raise ValueError("A nonempty sequence and a nonnegative bound are required.")


def bias_interval(
    observed: tuple[Fraction, ...],
    predicted: tuple[Fraction, ...],
    bias_bound: Fraction,
    error_bound: Fraction,
) -> Interval:
    validate_sequence(observed, bias_bound)
    validate_sequence(predicted, error_bound)
    if len(observed) != len(predicted):
        raise ValueError("Observation and prediction lengths must match.")
    lower, upper = -bias_bound, bias_bound
    for measured, expected in zip(observed, predicted):
        lower = max(lower, measured - expected - error_bound)
        upper = min(upper, measured - expected + error_bound)
    return lower, upper


def pair_gap(
    first: tuple[Fraction, ...],
    second: tuple[Fraction, ...],
    bias_bound: Fraction,
    error_bound: Fraction,
) -> Fraction:
    validate_sequence(first, bias_bound)
    validate_sequence(second, error_bound)
    if len(first) != len(second):
        raise ValueError("Prediction lengths must match.")
    lower, upper = -2 * bias_bound, 2 * bias_bound
    for left, right in zip(first, second):
        difference = left - right
        lower = max(lower, difference - 2 * error_bound)
        upper = min(upper, difference + 2 * error_bound)
    return lower - upper


def decode(
    observed: tuple[Fraction, ...],
    predictions: dict[str, tuple[Fraction, ...]],
    signatures: dict[str, Signature],
    bias_bound: Fraction,
    error_bound: Fraction,
) -> tuple[str, dict[str, Interval]]:
    if not predictions or predictions.keys() != signatures.keys():
        raise ValueError("Nonempty predictions and matching signatures are required.")
    if any(not signature for signature in signatures.values()):
        raise ValueError("Task signatures must not be empty.")
    if len({len(signature) for signature in signatures.values()}) != 1:
        raise ValueError("Task signature dimensions must match.")
    survivors = {}
    for name, prediction in predictions.items():
        interval = bias_interval(observed, prediction, bias_bound, error_bound)
        if interval[0] <= interval[1]:
            survivors[name] = interval
    classes = {signatures[name] for name in survivors}
    status = "model_conflict" if not survivors else (
        "task_resolved" if len(classes) == 1 else "ambiguous"
    )
    return status, survivors


BIAS_BOUND = Fraction("0.10")
ERROR_BOUND = Fraction("0.02")
PREDICTIONS = {
    "H1": tuple(map(Fraction, ("2.00", "2.04", "2.10", "2.00"))),
    "H2": tuple(map(Fraction, ("2.00", "2.00", "2.00", "2.00"))),
    "H3": tuple(map(Fraction, ("2.05", "2.09", "2.15", "2.05"))),
}
SIGNATURES = {
    "H1": (True, True, False),
    "H2": (True, False, True),
    "H3": (True, True, False),
}
PROGRESS = tuple(map(Fraction, ("0.00", "0.10", "0.20", "0.40")))


def candidate_rows() -> list[dict[str, object]]:
    speed = Fraction("0.20")
    latency = Fraction("0.20")
    deceleration = Fraction("0.60")
    margin = Fraction("0.10")
    processing = Fraction("0.10")
    hold = Fraction("1.00")
    distance = Fraction("0.80")
    local_time = Fraction("4.00")
    rows = []
    for count, progress in enumerate(PROGRESS, 1):
        gaps = [
            pair_gap(PREDICTIONS[left][:count], PREDICTIONS[right][:count],
                     BIAS_BOUND, ERROR_BOUND)
            for left, right in combinations(PREDICTIONS, 2)
            if SIGNATURES[left] != SIGNATURES[right]
        ]
        decision_time = progress / speed + processing
        stopping_distance = (
            speed * (decision_time + latency)
            + speed * speed / (2 * deceleration) + margin
        )
        full_time = decision_time + latency + speed / deceleration + hold
        minimum_gap = min(gaps)
        rows.append({
            "samples": count,
            "progress_m": float(progress),
            "decision_s": float(decision_time),
            "cross_class_gap_m": float(minimum_gap),
            "stop_distance_m": float(stopping_distance),
            "full_time_s": float(full_time),
            "task_separating": minimum_gap >= Fraction("0.01"),
            "straight_screen_pass": (
                stopping_distance <= distance and full_time <= local_time
            ),
        })
    return rows


class SequenceTests(unittest.TestCase):
    def test_exact_gaps(self) -> None:
        expected = tuple(map(Fraction, ("-0.08", "-0.04", "0.02", "0.02")))
        for count, gap in enumerate(expected, 1):
            self.assertEqual(
                pair_gap(PREDICTIONS["H1"][:count], PREDICTIONS["H2"][:count],
                         BIAS_BOUND, ERROR_BOUND),
                gap,
            )

    def test_same_task_modes_are_not_deleted(self) -> None:
        observed = tuple(map(Fraction, ("2.01", "2.05", "2.11")))
        status, survivors = decode(
            observed, {h: values[:3] for h, values in PREDICTIONS.items()},
            SIGNATURES, BIAS_BOUND, ERROR_BOUND,
        )
        self.assertEqual(status, "task_resolved")
        self.assertEqual(set(survivors), {"H1", "H3"})
        self.assertEqual(survivors["H1"], (Fraction("-0.01"), Fraction("0.03")))
        self.assertEqual(survivors["H3"], (Fraction("-0.06"), Fraction("-0.02")))

    def test_other_task_class(self) -> None:
        observed = (Fraction("2.01"),) * 3
        status, survivors = decode(
            observed, {h: values[:3] for h, values in PREDICTIONS.items()},
            SIGNATURES, BIAS_BOUND, ERROR_BOUND,
        )
        self.assertEqual((status, set(survivors)), ("task_resolved", {"H2"}))

    def test_single_frame_stays_ambiguous(self) -> None:
        status, _ = decode(
            (Fraction("2.01"),), {h: values[:1] for h, values in PREDICTIONS.items()},
            SIGNATURES, BIAS_BOUND, ERROR_BOUND,
        )
        self.assertEqual(status, "ambiguous")

    def test_all_invalid_is_reported(self) -> None:
        status, survivors = decode(
            (Fraction("9"),) * 3,
            {h: values[:3] for h, values in PREDICTIONS.items()},
            SIGNATURES, BIAS_BOUND, ERROR_BOUND,
        )
        self.assertEqual((status, survivors), ("model_conflict", {}))

    def test_touching_tubes_are_not_separated(self) -> None:
        self.assertEqual(
            pair_gap((Fraction("0"), Fraction("0.08")),
                     (Fraction("0"), Fraction("0")), BIAS_BOUND, ERROR_BOUND),
            0,
        )

    def test_constant_offset_can_remain_ambiguous(self) -> None:
        self.assertLessEqual(
            pair_gap(PREDICTIONS["H1"], PREDICTIONS["H3"],
                     BIAS_BOUND, ERROR_BOUND),
            0,
        )

    def test_independent_frame_biases_hide_sequence_conflict(self) -> None:
        observed = tuple(map(Fraction, ("2.01", "2.05", "2.11")))
        predicted = PREDICTIONS["H2"][:3]
        for measured, expected in zip(observed, predicted):
            lower, upper = bias_interval(
                (measured,), (expected,), BIAS_BOUND, ERROR_BOUND
            )
            self.assertLessEqual(lower, upper)
        lower, upper = bias_interval(
            observed, predicted, BIAS_BOUND, ERROR_BOUND
        )
        self.assertGreater(lower, upper)

    def test_absolute_bias_bound_retains_evidence_lost_by_differencing(self) -> None:
        predicted = PREDICTIONS["H1"][:3]
        observed = tuple(value + Fraction("0.50") for value in predicted)
        self.assertEqual(
            tuple(value - observed[0] for value in observed),
            tuple(value - predicted[0] for value in predicted),
        )
        lower, upper = bias_interval(
            observed, predicted, BIAS_BOUND, ERROR_BOUND
        )
        self.assertGreater(lower, upper)

    def test_one_task_class_retains_all_compatible_positions(self) -> None:
        status, survivors = decode(
            (Fraction("2.01"),),
            {name: values[:1] for name, values in PREDICTIONS.items()},
            {name: SIGNATURES["H1"] for name in PREDICTIONS},
            BIAS_BOUND, ERROR_BOUND,
        )
        self.assertEqual(status, "task_resolved")
        self.assertEqual(set(survivors), set(PREDICTIONS))

    def test_large_error_removes_separation(self) -> None:
        self.assertLessEqual(
            pair_gap(PREDICTIONS["H1"][:3], PREDICTIONS["H2"][:3],
                     BIAS_BOUND, Fraction("0.03")),
            0,
        )

    def test_no_false_exclusion_inside_declared_bounds(self) -> None:
        errors = (-ERROR_BOUND, Fraction(0), ERROR_BOUND)
        for prediction in PREDICTIONS.values():
            for bias, noise in product(
                (-BIAS_BOUND, Fraction(0), BIAS_BOUND), product(errors, repeat=3)
            ):
                observed = tuple(
                    value + bias + perturbation
                    for value, perturbation in zip(prediction[:3], noise)
                )
                lower, upper = bias_interval(
                    observed, prediction[:3], BIAS_BOUND, ERROR_BOUND
                )
                self.assertLessEqual(lower, bias)
                self.assertGreaterEqual(upper, bias)

    def test_earliest_enumerated_probe(self) -> None:
        valid = [row for row in candidate_rows()
                 if row["task_separating"] and row["straight_screen_pass"]]
        self.assertEqual(valid[0]["samples"], 3)
        self.assertEqual(valid[0]["progress_m"], 0.2)
        self.assertAlmostEqual(valid[0]["stop_distance_m"], 0.3933333333333333)
        self.assertAlmostEqual(valid[0]["full_time_s"], 2.6333333333333333)

    def test_invalid_input_is_not_silently_truncated(self) -> None:
        with self.assertRaises(ValueError):
            bias_interval((Fraction(1),), (Fraction(1), Fraction(2)),
                          BIAS_BOUND, ERROR_BOUND)
        with self.assertRaises(ValueError):
            pair_gap((), (), BIAS_BOUND, ERROR_BOUND)
        with self.assertRaises(ValueError):
            pair_gap((Fraction(1),), (Fraction(1),), Fraction(-1), ERROR_BOUND)
        with self.assertRaises(ValueError):
            decode((Fraction(1),), {}, {}, BIAS_BOUND, ERROR_BOUND)
        with self.assertRaises(ValueError):
            decode((Fraction(1),), {"H1": (Fraction(1),)}, {},
                   BIAS_BOUND, ERROR_BOUND)
        with self.assertRaises(ValueError):
            decode((Fraction(1),), {"H1": (Fraction(1),)}, {"H1": ()},
                   BIAS_BOUND, ERROR_BOUND)
        with self.assertRaises(ValueError):
            decode((Fraction(1),), {"H1": (Fraction(1),), "H2": (Fraction(1),)},
                   {"H1": (True,), "H2": (True, False)}, BIAS_BOUND, ERROR_BOUND)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--test", action="store_true", help="Run exact arithmetic tests.")
    args = parser.parse_args()
    if args.test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(SequenceTests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        raise SystemExit(0 if result.wasSuccessful() else 1)
    observed = tuple(map(Fraction, ("2.01", "2.05", "2.11")))
    status, survivors = decode(
        observed, {h: values[:3] for h, values in PREDICTIONS.items()},
        SIGNATURES, BIAS_BOUND, ERROR_BOUND,
    )
    print(json.dumps({
        "scope": "offline scalar kernel; straight stopping screen only",
        "candidates": candidate_rows(),
        "status": status,
        "survivors": {h: list(map(float, interval)) for h, interval in survivors.items()},
    }, indent=2))


if __name__ == "__main__":
    main()
