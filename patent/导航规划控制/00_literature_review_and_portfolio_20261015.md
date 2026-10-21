# 导航规划控制专利组合与文献检索台账

> 检索基准日：2026-10-15。
> 交付版本：V2.0；三篇交底书及三份逐案独立技术详解，保留前两轮检索并追加机器人来源驱动修订。
> 证据范围：16 篇核心论文、7 件核心专利、2 份官方工程文档；论文中 7 篇核读相关方法正文，9 篇核读摘要；7 件专利均核读书目及相关权利要求。
> 性质：研发与代理沟通草案，非授权、新颖性或自由实施法律意见。
> 适用对象：移动机器人及车辆。A/C 最小实现选地面 AMR，B 给出轮式和足式接触控制支撑；足式/飞行扩展须各自验证，不推定已有实机实现。
> 2026-10-20 文档同步：下列 A/B/C 第一、第二部分按模板职责统一。历史检索基准及证据数量不因此更新；2026-10-19 补充核验以各模板稿第七部分为准。

## 1. 交付目录与阅读顺序

| 案件 | 完整交底书 | 拟保护的技术链路 | 近期直接对比 |
| --- | --- | --- | --- |
| A | [01_patent_a_occlusion_handover_certificate_disclosure_20261015.md](01_patent_a_occlusion_handover_certificate_disclosure_20261015.md) | 实际驱动队列/代际/备份确认参与的接管过渡验证及有限前缀执行；高创新风险 | L12 OcclusionCBF、L13 gatekeeper 综述与 P02/P07 均有紧邻披露 |
| B | [02_patent_b_friction_evidence_consistent_planning_disclosure_20261015.md](02_patent_b_friction_evidence_consistent_planning_disclosure_20261015.md) | 轮端或足端接触证据适用域、段/支撑相依赖撤销、上下游重验、同快照执行 | P03/P06；L14 足端机会约束、L15/L16 在线适应及全身反馈 |
| C | [03_patent_c_local_frame_route_handover_disclosure_20261015.md](03_patent_c_local_frame_route_handover_disclosure_20261015.md) | 地图失配后任务出口/权限共同前缀、动作承诺及完整局部有效时域、重验回切 | L03/L08/L10、P04/P05、D01 坐标规范 |

| 案件 | 单独新建的来源与完整技术详解 | 建议阅读内容 |
| --- | --- | --- |
| A | [01_patent_a_sources_and_technical_principles_20261015.md](01_patent_a_sources_and_technical_principles_20261015.md) | 接管三段时序、可恢复集合、队列/激活接口、差速动力学、两种队列的前缀反例 |
| B | [02_patent_b_sources_and_technical_principles_20261015.md](02_patent_b_sources_and_technical_principles_20261015.md) | 摩擦椭圆/足端锥、质心与全身动力学、证据图和撤销、机会约束、AMR/四足案例 |
| C | [03_patent_c_sources_and_technical_principles_20261015.md](03_patent_c_sources_and_technical_principles_20261015.md) | map/odom 权限与副本、多假设共同动作、空间/时间停止条件、室内门口与回切反例 |

上表的三份 20261015 历史交底书各含 12 个一级章节：摘要、现有技术、问题、最小技术组合、模块接口、实施步骤、数值实施例、附图、区别与风险、权利要求建议、验证计划、迭代及补证。每案附两幅 Mermaid 示意图。摘要和权利要求为建议稿，不是正式申请文件。

### 当前七部分模板稿与同步范围

| 案件 | 当前模板编排 | 第一部分：缺点/原因→目的/效果 | 第二部分：结构/原理→针对性不足 |
| --- | --- | --- | --- |
| A | [接管与短段许可](01_patent_a_disclosure_template_rewrite_20261019.md) | 漏算旧输入、条件错配、期限高估→按真实接管过程限定可执行长度 | 主备检查与驱动执行链；主要对比 gatekeeper，结合隐藏占用和时效检查分析接口缺口 |
| B | [能力变化与运动计划切换](02_patent_b_disclosure_template_rewrite_20261019.md) | 过渡未覆盖、前后段不衔接、规划/用力不一致→从实际生效状态关联重验 | 估计/分区→规划→力分配→驱动；主要对比 CN120552911B，明确完整覆盖可以替换旧安排 |
| C | [定位异常与入口限制](03_patent_c_disclosure_template_rewrite_20261019.md) | 参考突变、入口身份/权限不明、停止全过程依据不足→有限局部接管 | 坐标/任务→多解释规划→底盘；主要对比多位置解释动作规划，结合 REP-105 和导航约束 |

第一部分只列本案处理的缺点，并说明原因、正面的技术问题及对应效果；各交底书第二部分统一只设“2.1 技术背景”和“2.2 现有技术方案及缺点”：前者交代应用和系统组成，后者合并说明主要方案的工作原理、针对性不足及出处，不另设重复归纳表或逐项对应表。完整书目留在模板稿第七部分、技术详解及本台账。不能把未解决的限制写成本案已解决的问题，不能将“本轮没读到”当作“先例没有”。

历史十二节稿保留原编排：第 3 节承接模板第一部分，第 2 节承接模板第二部分；三份技术详解在第 1 节补充缺点—原因—效果对应，在第 2 节补充已有结构及原理，原公式和算例保留。需要按模板交付时优先使用上表七部分稿。

B 案所有文档中的“撤销旧批准”均指停止凭旧依据追加动作；完整覆盖是实现方式之一，不要求独立撤销报文，也不意味着已有速度或接触力瞬间消失。已完整覆盖并核对过渡的方案不能被错误列为仍有该缺点。

以理解为目标，先读对应详解第 1-3 节的直观问题、来源矩阵和架构，再读原理、实现和算例，最后核对交底书第 4、9、10 节保护边界。每份详解独立含 14 节、自足参考文献、接口、伪代码和失败处理。发明人、申请人、形成时间、平台与控制器参数必须按真实记录补入。

## 2. 检索范围与最新性边界

使用 arXiv 公告时间倒序检索、摘要页版本历史、可访问论文 HTML 正文、Google Patents 检索索引和公开全文。近期线索优先覆盖 2025-2026 年，但保留能直接削弱宽泛创新主张的早期基础文献。

本轮实际核验的近期更新包括：L01 v3（2026-10-05）、L04 首稿（2026-10-02）、L10 v2（2026-10-02）、L05 首稿（2026-07-11），以及 P05 授权公告（2026-04-07）、P06 授权公告（2026-02-06）。论文首稿、修订、期刊出版和专利申请公布、授权公告分别记录，不混作同一种“发表时间”。

V2.0 追加核验 L12 首稿 2026-09-06、L13 v2 2026-09-18；L11/L14-L16 为相关多平台及足式基础，不为了“最新”删去直接影响创新判断的旧来源。新增机器人论文检索没有同步完成机器人专利分类全量扩展，不能因已有车辆专利可类比就认定机器人领域没有更近专利。

不声称这些是全球最新的全部成果，也不声称三案具有已被法律确认的新颖性。未公开申请、数据库延迟、非英语/中文文献、全文不可检索附件、同族差异和检索语义遗漏均可能影响结论。CNIPA、WIPO、Espacenet、USPTO 的官方档案与审查意见尚未逐件复核。

访问与过滤限制：

- Google 通用搜索抓取无有效正文，浏览器访问一度超时；Bing 返回页面框架但无有效结果，不作为完成检索的证据。
- Google Patents 正文抓取部分返回 503，P04-P06 后通过浏览器取得有效书目及权利要求。
- 末轮尝试 `after=publication:20250101`、`before=publication:20261016`、`sort=new` 的结构化检索，返回记录包含 2015、2018 年专利，日期筛选和排序未得到验证。该轮只作为过滤失败记录，不能据此认定“2026 年 10 月前最新专利已查全”。
- 各核心来源中的日期均由具体摘要页或全文书目核对，不以检索排序代替日期验证；L04 索引曾显示 10 月 1 日，原始提交历史为 10 月 2 日，本台账采用后者。
- L12 索引日期与原始 UTC 提交历史有一天差异，本版采用 2026-09-06；L15 v2 采用原始历史 2025-11-30。D01 网页及部分 ROS 文档返回防爬页，实际读取其公开官方源文本；错误 Nav2 配置路径返回 404，不计作正文已读。

## 3. 可复现检索路径

检索日期均为 2026-10-15。以下结果数只描述本次界面返回，不代表数据库完整规模或去重后文献数；没有逐页遍历的检索不写成穷尽检索。

| 轮次 | 数据源与检索式 | 实际处理及用途 |
| --- | --- | --- |
| R1-A | [arXiv: contingency planning autonomous driving](https://arxiv.org/search/?query=contingency+planning+autonomous+driving&searchtype=all&order=-announced_date_first&size=25) | 返回 16 条；核验 L01、L02，并从 L01 正文追踪更早双轨迹与可达性工作 |
| R1-B1 | [arXiv: friction motion planning](https://arxiv.org/search/?query=friction+motion+planning&searchtype=all&order=-announced_date_first&size=25) | 返回 80 条，核查首页；大量操纵类结果，转向更窄轮胎检索，不据此证明车辆文献缺失 |
| R1-B2 | [arXiv: tire friction uncertainty](https://arxiv.org/search/?query=tire+friction+uncertainty&searchtype=all&order=-announced_date_first&size=25) | 返回 13 条；核验 L05-L07，排除不相关机械对象 |
| R1-C | [arXiv: localization uncertainty motion planning](https://arxiv.org/search/?query=localization+uncertainty+motion+planning&searchtype=all&order=-announced_date_first&size=25) | 返回 96 条，核查首页；核验 L03、L04、L08，不采用撤稿条目作为本案实证 |
| R1-P | Google Patents：`contingency trajectory planning`、`friction trajectory planning`、`localization uncertainty planning` | 读取结构化结果后逐件进入核心专利；沿 P01、P02 引证及相似文献追踪 P04、P05、P07 |
| R2-A | [arXiv: backup trajectory latency safety](https://arxiv.org/search/?query=backup+trajectory+latency+safety&searchtype=all&order=-announced_date_first&size=25) | 本次无结果；不能推断不存在同义先例；重点回读 P07 全文 |
| R2-B | [arXiv: friction constraint invalidation](https://arxiv.org/search/?query=friction+constraint+invalidation&searchtype=all&order=-announced_date_first&size=25) | 返回 2 条；核验相关 L09 摘要；同时取得 P06 中文权利要求并修订 B 案 |
| R2-C | [arXiv: navigation topological ambiguity](https://arxiv.org/search/?query=navigation+topological+ambiguity&searchtype=all&order=-announced_date_first&size=25) | 返回 17 条；核验 L10 原始历史及摘要，修订多假设和提交边界 |
| R2-P | Google Patents 上述三主题，尝试近期公开日过滤及新近排序 | 返回日期范围外文献，过滤失败；没有把其返回顺序写成最新排名 |
| R3-A | 机器人备份/遮挡关键词线索后逐条核验 [DYNUS](https://arxiv.org/abs/2504.16734)、[OcclusionCBF](https://arxiv.org/abs/2609.06342)、[备份过滤综述](https://arxiv.org/abs/2604.02401)，并追踪综述引文 | 核读 L12/L13 相关正文，确认最大名义时长和倒计时已有公开；原始 gatekeeper 引文仅间接核对，未计为新增核心全文 |
| R3-B | 四足摩擦/MPC 关键词后逐条核验 [L14](https://arxiv.org/abs/2411.03481)、[L15](https://arxiv.org/abs/2510.15626)、[L16](https://arxiv.org/abs/1905.06144) | L14 正文 III-V 作为足端约束和分层控制来源，L15/L16 保持摘要级；不将动态遗憾当安全保证 |
| R3-D | 从官方源仓库读取 REP-105 和 Nav2 Collision Monitor README | D01/D02 明确局部连续可漂移、TF 权限、速度过滤及非硬实时认证边界；动态分支未固定提交 |

arXiv 按公告时间排序主要反映首版公告年月，不保证最近修订优先；因此必须单独读取已有强相关论文的版本历史。

后续官方检索建议结合 B60W60/00、B60W30/09、B60W40/06、G05D1/00、G01C21/00、B25J 等入口及“机器人备份接管、执行队列、接触证据、支撑相撤销、全身控制一致性、重定位失配、任务出口歧义”等同义词，继续做申请人、同族和引证扩展。分类仅为入口建议，未完成其全部检索，也未核对所有新版分类细目。

## 4. 核心论文清单

状态说明：“正文”仅代表核读表列相关章节，不代表已复现算法、核实作者全部实验或完成逐式审稿；“摘要”不支持对未读正文作否定披露判断。预印本不自动等于同行评审成果。

| 编号 | 作者、题名及原始链接 | 首次提交 / 本轮核验版本 | 证据深度及实际用途 |
| --- | --- | --- | --- |
| L01 | Lei Zheng, Rui Yang, Minzhe Zheng, Zengqi Peng, Michael Yu Wang, Jun Ma. [Occlusion-Aware Contingency Safety-Critical Planning for Autonomous Driving](https://arxiv.org/abs/2502.06359) | 2025-02-10 / v3 2026-10-05；页面列 IEEE Transactions on Cybernetics 56(5), 2777-2790，2026；DOI 10.1109/TCYB.2025.3632366 | [正文](https://arxiv.org/html/2502.06359v3) II-A、III、IV、V；双轨迹、共享段、固定共识步长及其局限；缩尺机器人实验不能写成本案实车验证 |
| L02 | Rui Yang, Lei Zheng, Shuzhi Sam Ge, Jun Ma. [Safe and Nonconservative Contingency Planning for Autonomous Vehicles via Online Learning-Based Reachable Set Barriers](https://arxiv.org/abs/2509.07464) | 2025-09-09 / v2 2026-04-15；页面列 TCST 2026；DOI 10.1109/TCST.2026.3675339 | 摘要；事件触发意图集更新与可达集屏障，提示不能独占在线不确定性适应 |
| L03 | Tommaso Faraci, Marco Camurri, Daniele Fontanelli, Luigi Palopoli. [UNSEEN: Uncertainty-aware Navigation via Sparse Estimation in Unknown Environments](https://arxiv.org/abs/2606.20755) | 2026-06-18 / v1 | [正文](https://arxiv.org/html/2606.20755v1) III-VII；相关不确定性、可见域截断、感知规划；实际采用 RGB-D，无人机静态室内验证 |
| L04 | Luis Marques, Rong Fang, Disha Kamale, Dmitry Berenson. [Localized Conformal Safety Monitoring with Vision-Language Models for Autonomous Driving](https://arxiv.org/abs/2610.02765) | 2026-10-02 / v1；5 页 extended abstract | 摘要；SLLCP 校准、可交换性前提；不把概率覆盖写成车辆必然无碰撞 |
| L05 | Bongsob Song. [Diffusion-Residual Model Predictive Steering Control for Vehicle Stabilization at the Limit of Handling under Model Uncertainty](https://arxiv.org/abs/2607.10243) | 2026-07-11 / v1；页面标注投稿 TCST，不按已录用处理 | [正文](https://arxiv.org/html/2607.10243v1) II-IV、V-E、VI；参考与约束修正、软约束可解边界、实测运行时间而非静态时延上界 |
| L06 | Alexander Davydov, Franck Djeumou, Marcus Greiff, Makoto Suminaka, Michael Thompson, John Subosits, Thomas Lew. [First, Learn What You Don't Know: Active Information Gathering for Driving at the Limits of Handling](https://arxiv.org/abs/2411.00107) | 2024-10-31 / v2 2025-07-23 | 摘要；主动采集与在线适应不足，提醒不能假设未知附着能被即时学准 |
| L07 | Sean Vaskov, Rien Quirynen, Marcel Menner, Karl Berntorp. [Friction-Adaptive Stochastic Nonlinear Model Predictive Control for Autonomous Vehicles](https://arxiv.org/abs/2305.03798) | 2023-05-05 / v1 | 摘要；贝叶斯轮胎模型与不确定性进入 SNMPC 的基础先例，非最新成果 |
| L08 | Pritom Gogoi, Faris Janjos, Bin Yang, Andreas Look. [Uncertainty Matters: Structured Probabilistic Online Mapping for Motion Prediction in Autonomous Driving](https://arxiv.org/abs/2603.20076) | 2026-03-20 / v1 | [正文](https://arxiv.org/html/2603.20076v1) III-V；LRPD 相关几何、nuScenes 离线建图/预测；不当作闭环导航实证 |
| L09 | Yurun Gan, Ziyu Song, Jing Yang, Zheng Lin, Jianuo Zhang, Tongtong Gu, Haitao Ding, Nan Xu, Por Lip Yee, Wei Ni, Jun Luo. [Dual-Envelope Constrained Nonlinear MPC for Distributed Drive Electric Vehicles Drifting Under Bounded Steering and Direct Yaw-Moment Control](https://arxiv.org/abs/2604.07342) | 2026-04-08 / v1 | 摘要；转向与横摆输入耦合改变可恢复稳定域，促使 B 案新增输入条件依赖 |
| L10 | Jiaming Wang, Jizhuo Chen, Diwen Liu, Atharva Ghotavadekar, Jiaxuan Da, Linh Kastner, Harold Soh. [Change-Robust Online Topological Memory for Long-Term Relocalization and Semantic Navigation](https://arxiv.org/abs/2605.02227) | 2026-05-04 / v2 2026-10-02；作者页面标注 NeurIPS 2026 接收，本轮未独立核会议名录 | 摘要；CROSS 多位姿分支及地图关联提交前验证，促使 C 案收窄并加入提交撤销 |
| L11 | Kota Kondo, Mason Peterson, Nicholas Rober, Juan Rached Viso, Lucas Jia, Jialin Chen, Harvey Merton, Jonathan P. How. [DYNUS: Uncertainty-aware Trajectory Planner in Dynamic Unknown Environments](https://arxiv.org/abs/2504.16734) | 2025-04-23 / v3 2025-05-18 | 摘要；探索/安全/应急轨迹、轮式/四足/飞行平台；不将多平台验证转作本案结果 |
| L12 | Taekyung Kim, Hun Kuk Park, Renya Wada, Nikolay Atanasov, Shumon Koga, Dimitra Panagou. [OcclusionCBF: Backup Control Barrier Functions for Safe Navigation Among Hidden Dynamic Obstacles](https://arxiv.org/abs/2609.06342) | 2026-09-06 / v1 | [正文](https://arxiv.org/html/2609.06342v1) II-IV、V-D；直接覆盖隐藏占用、备份与验证终端；IV-E 说明有限采样不自动继承连续保证 |
| L13 | Taekyung Kim, Aswin D. Menon, Akshunn Trivedi, Dimitra Panagou. [Backup-Based Safety Filters: A Comparative Review of Backup CBF, Model Predictive Shielding, and gatekeeper](https://arxiv.org/abs/2604.02401) | 2026-04-02 / v2 2026-09-18；页面列 CDC 2026，未独立核会议记录 | [正文](https://arxiv.org/html/2604.02401v2) II-VI；gatekeeper 最长切换时间、有状态递减及 MPS/Backup CBF 比较；A 案须据此显著收窄 |
| L14 | Ananya Trivedi, Sarvesh Prajapati, Mark Zolotas, Michael Everett, Taskin Padir. [Chance-Constrained Convex MPC for Robust Quadruped Locomotion Under Parametric and Additive Uncertainties](https://arxiv.org/abs/2411.03481) | 2024-11-05 / v1 | [正文](https://arxiv.org/html/2411.03481v1) III-V；SRBD、接触机会锥、摆动足零力、Go1；油面实验调整速度/摩擦，不能泛称所有地面无需调整 |
| L15 | Hongyu Zhou, Xiaoyu Zhang, Vasileios Tzoumas. [Adaptive Legged Locomotion via Online Learning for Model Predictive Control](https://arxiv.org/abs/2510.15626) | 2025-10-17 / v2 2025-11-30 | 摘要；随机 Fourier 特征/最小二乘在线残差及 MPC，Gazebo/MuJoCo；动态遗憾非物理安全保证 |
| L16 | Ruben Grandia, Farbod Farshidian, Rene Ranftl, Marco Hutter. [Feedback MPC for Torque-Controlled Legged Robots](https://arxiv.org/abs/1905.06144) | 2019-05-15 / v2 2019-08-09；页面列 IROS 2019 | 摘要；反馈桥接 MPC 与高频力矩、摩擦约束与带宽，足式基础先例 |

作者姓名在本台账中部分去除变音符以便文本检索，标准拼写可从原始页面获取。论文中的实验提升率和运算时间均未作为本案已实现效果。

## 5. 核心专利清单

“公开日”与“授权公告日”分列；日期为对应文献，不保证是专利族全球最早公开日。申请主体列为检索/正文显示值而非已核验的现时权利人。

| 编号 | 题名及全文 | 公开文本与日期 | 相关授权文本与日期 | 主体与核读位置 |
| --- | --- | --- | --- | --- |
| P01 | [Contingency planning and security](https://patents.google.com/patent/JP7401650B2/en)；同族英文题名含 Contingency Planning and Safety Assurance | JP2022542277A，2022-09-30；页面同族表列 US20210031760A1、WO2021021269A1 均 2021-02-04 | JP7401650B2，2023-12-19；优先权 2019-07-31 | 索引与全文主体不同，全文列 Renault SAS，索引见 Nissan North America；归属待官方核对。核读权利要求 1、8、图 22/26 说明；已含反应时间与遮挡停止能力 |
| P02 | [System and method for trajectory validation](https://patents.google.com/patent/US11407409B2/en) | US20210046923A1，2021-02-18 | US11407409B2，2022-08-09；优先权 2019-08-13 | Zoox；权利要求 1、6、16 及图 3/11/14；轨迹过期、准时、一致、动态能力及备份管理 |
| P03 | [Driving surface friction estimations for autonomous vehicles](https://patents.google.com/patent/US11427223B2/en) | US20200089243A1，2020-03-19 | US11427223B2，2022-08-30；优先权 2018-09-14 | 页面见 UATC LLC、Volvo Car Corp；权利要求 1-6、11-13、18-20、图 2/12-14；置信度随时间下降和分轮自然事件估计已知 |
| P04 | [Adaptive mapping to navigate autonomous vehicles responsive to physical environment changes](https://patents.google.com/patent/US9612123B1/en) | 本轮核验 B1 公开，不另推断未核实的 A 文本 | US9612123B1，2017-04-04；页面列申请/优先权 2015-11-04，完整链未查 | Zoox；浏览器核读权利要求 1-5、16，地图差异、混合地图、更新及远程请求 |
| P05 | [Navigational constraint control system](https://patents.google.com/patent/US12594960B2/en) | US20240149912A1，2024-05-09 | US12594960B2，2026-04-07；优先权 2022-11-03 | Nissan North America；浏览器核读权利要求 1、7、12-20；导航不确定、虚拟遮挡对象、横纵限制、优先减速 |
| P06 | [基于多源数据融合的无人驾驶动态路径规划方法及系统](https://patents.google.com/patent/CN120552911B/zh) | CN120552911A，2025-08-29 | CN120552911B，2026-02-06；申请/优先权 2025-05-20 | 索引为河南海融软件有限公司，正文英文 Henan Hisoft Software Co ltd，中文法定名称待官方核对；权利要求 1、4-7；附着场、力椭圆、前后轴分配和 MPC 同步更新 |
| P07 | [Safe system operation using latency determinations](https://patents.google.com/patent/US11099573B2/en) | US20200201335A1，2020-06-25 | US11099573B2，2021-08-24；优先权 2018-12-19 | Zoox；权利要求 1、8-9、17-19 及图 6；标签追踪、时延统计阈值和安全状态；从相似表取得的 B1 后缀已更正 |

上述为公开全文中的技术披露比较，不把授权权利要求未包含的说明书内容当作“未公开”；也不因美国申请放弃、WO 状态终止等原因就忽略其在先公开效力。

仍需跟进的非核心线索：CN113632033B（车辆控制方法和装置）、CN114596360B（图拓扑主动定位建图，英文索引题名未定稿）曾在结果出现，但全文抓取失败，未据其摘要作排除结论；P01 的 CN114175023A 等同族应回到官方文本逐项核查。这些不计入 7 件核心全文专利。

### 5.1 官方工程来源

| 编号 | 文档及原始来源 | 实际核读及使用边界 |
| --- | --- | --- |
| D01 | Wim Meeussen，REP-105: Coordinate Frames for Mobile Platforms；2010-10-27，Active/Informational；[官方源文](https://raw.githubusercontent.com/ros-infrastructure/rep/master/rep-0105.rst) | 读取帧语义、Frame Authorities、Transitions Between Maps；`odom` 可无界漂移、`map` 可跳变，单一变换权威和电梯语义均为已有约定 |
| D02 | Navigation2 project，Nav2 Collision Monitor；[官方 README](https://raw.githubusercontent.com/ros-navigation/navigation2/main/nav2_collision_monitor/README.md) | 读取 Features、Design、Metrics；独立过滤 cmd_vel、停止/减速/TTC；官方明确不提供硬实时安全认证 |

两者访问于 2026-10-15，均为动态源分支而非固定提交或发行版。未核定软件许可适配和安全合规；不能将文档示例运行时间当作本案端到端最坏耗时。

## 6. 反例驱动的收敛与实际修订

| 案件 | 首轮宽泛设想与反例 | 初稿 V1.0 的收敛 | 第二轮新增证据及实际 V1.1 修订 |
| --- | --- | --- | --- |
| A | 遮挡感知、双轨迹和共享前缀已由 L01 披露；反应时间与过期验证见 P01/P02 | 接管过渡管包含于未来备份可接管集合，反算主轨迹可执行前缀 | 核读 P07 后增加“时延未异常但接管已不可达”的对照，纠正 B1/B2；补齐整个停止时域覆盖和统计时延保证边界 |
| B | 附着不确定性 MPC 见 L07；自然激励、分轮动作及置信度衰减见 P03 | 附着证据适用域与轮轨迹段依赖撤销、同版本规划分配执行 | 核读 P06 权利要求后删除附着场、前后轴分配和控制器同步的首创暗示；依据 L09 补输入耦合重验；补指令代际、生效时刻和队列撤销过渡 |
| C | 感知导航与不确定性传播见 L03/L08；地图差异见 P04；横纵限制见 P05 | 合理出口假设共同前缀、不可逆分叉停止边界、连续局部接管与重验回切 | 核读 L10 摘要后将多假设和延迟提交归为已有方向；加入出口提交撤销、相关重复误匹配及完整停止时域误差增长约束 |

V2.0 的第三轮实际修订：

| 案件 | 新增来源带来的实质修订 | 新建详解及机器人实现支撑 |
| --- | --- | --- |
| A | L12/L13 推翻“最长前缀＋备份＋倒计时可作主要新点”的推断；承认高创新风险，仅保留队列/代际/实际激活闭环作为待核查候选 | 差速模型、外形/角运动、驱动接口；同样时延下匀速与加速旧队列分别只允许 0.16/0.10 s 示例 |
| B | L14-L16 明确足端 MPC 和分层全身反馈已有先例；不把换为四足当创新 | 通用 ContactEvidence、接触相依赖、足端锥、质心/全身动力学；AMR 和四足低摩擦撤证例 |
| C | D01 明确双帧是公开约定，连续 odom 可无界漂移；原始 TF 与任务对齐副本分开 | 相似门口/权限、可回退性决定承诺边界；空间够但完整停止时域不够的 AMR 反例 |

## 7. 技术假设、保护分工与风险

| 案件 | 待检验机制 | 能推翻假设的证据或测试 |
| --- | --- | --- |
| A | 已知备份过滤基础上，实际驱动队列与激活反馈是否产生未披露且非显而易见的控制闭环 | L12/L13 已覆盖抽象骨架；原始 gatekeeper/异步架构若覆盖队列绑定则需继续收窄或停止按当前组合申请 |
| B | 局部接触证据撤销经轨迹段/支撑相依赖改变速度、落足、力分配和确认生效 | 相同依赖链已有完整披露；或摩擦/模式变化后仍跨版本、用摆动足承载、忽略旧队列 |
| C | 任务出口/权限共同动作与完整局部有效时域共同限制接管及承诺 | 在先公开相同链路；或歧义未解仍越界、把连续 odom 当误差有界、失效后才停车 |

三案可分别实施：A 不要求使用 B 的附着估计器，底盘能力可来自既有接口；B 不要求遮挡或地图失配；C 不要求 A 的证书格式或 B 的证据图。联合部署时可交换保守底盘能力和有效走廊，但独立权利要求不应互相依赖才具备完整实施链路。

最小原型建议：A 选带驱动队列反馈的直线差速 AMR，B 先选轮式撤证闭环再评估足式全身接口，C 选单楼层两假设/一个门口。A 创新风险尤其高，先做原始 gatekeeper 和异步架构对比，再投入申请；平台扩展不提高当然授权概率。

三案均存在较强的创造性组合风险：可达性监督、依赖传播、版本一致性、假设树与局部坐标本身均非新概念。当前不能据“未在已读来源找到全部组合”宣布具有专利法上的新颖性或创造性；需要单篇对照新颖性分析、最接近文献及结合动机分析，和官方同族权利要求的自由实施评估。

## 8. 已做检查与未做验证

已逐案执行首次写入、V1.1 回归及 V2.0 交底书/独立详解的算术和结构检查：

| 案件 | 复算项目 | 结果与含义 |
| --- | --- | --- |
| A | 8 m/s、0.20 s 接管、3 m/s² 保证减速、1.5 m 裕量 | 停止所需 13.767 m；14 m 可用距离下最多等待约 0.029 s；接管增至 0.30 s 后需 14.567 m，应拒绝原放行 |
| B | 单轮载荷 4000 N、附着下界 0.25、裕量 0.8、横向需求 500 N | 纵向力上限 624.5 N；错误采用 0.70 则得到 2183.5 N；降至 0.15 后横向需求本身已不可行 |
| B | 20 m 内将速度降至 8 m/s，保证减速 2 m/s² | 忽略时延的上游筛查上界 12 m/s，当前 15 m/s 时不能靠修改目标速度宣称可行 |
| C | 9 m 分叉前停止、0.25 s 时延、2 m/s² 减速、误差及裕量合计 1 m | 速度筛查上界 5.179 m/s；5 m/s 需 8.5 m；6 m/s 需 11.5 m，不能承诺在原边界前停住 |
| C | 3.6 m 走廊、1.9 m 车宽、0.25 m 误差、0.20 m 裕量 | 中心轨迹每侧余量 0.40 m；误差增至 0.70 m 时余量 -0.05 m，拒绝继续依赖原走廊 |
| A 机器人 | 1.2 m/s、0.15 s、0.8 m/s²、净距离 1.5 m、裕量 0.2 m、监督周期 0.02 s | 匀速旧队列需求 1.28 m、工程前缀 0.16 s；过渡仍加速 0.3 m/s² 时需求 1.352140625 m、前缀 0.10 s；时延改 0.35 s 则立即需求 1.52 m，拒绝 |
| B 机器人 | 160 kg AMR，两驱动轮各载荷 400 N，裕量 0.8；摩擦下界 0.5 降 0.15 | 每轮切向能力上界 160 N 降 48 N，整体加速度必要上界 0.6 m/s²；1 m/s、0.12 s、裕量 0.15 m 时，即便乐观满能力也至少需 1.1033 m |
| B 足式 | 20 kg 四足水平均分支撑，裕量 0.8，摩擦下界 0.4 降 0.15 | 每足法向 49.05 N，切向上界 15.696 N 降 5.886 N；总水平加速度必要上界 1.1772 m/s²，原 2 m/s² 请求不可行；未证明全身可行 |
| C 机器人 | 0.8 m/s、0.2 s、0.6 m/s²、净距离 1.2 m，误差/裕量 0.25 m | 必要距离 0.9433 m，接管至停止需 1.5333 s；局部只有效 1.4 s 时仍拒绝完整保证；1.4 m 走廊/0.6 m 机身等参数下侧余量 0.20 m |

检查范围包括交底书各 12 节、详解各 14 节、围栏闭合、来源编号映射、本地链接及编辑器诊断；通过只表示文档完整性及示例算术一致，不代表公式证明或专利质量认证。Mermaid 为流程源图，未进行专门渲染器预览。

未做：完整算法实现、求解器测试、统计显著性测试、机器人/车辆动力学仿真、硬件在环、实机标定、安全认证、专业查新或侵权评价。各案验证计划可作为研发实验清单，不把计划中的样本数、论文成功率或其硬件能力写成本案成果。

## 9. 申请前的必要补证

1. 从官方数据库下载核心专利公布/授权原文及审查档案，核对同族、申请主体和真实优先权链；特别关注 P01/P06 的主体差异。
2. 补读仅摘要核验的 L02/L04/L06/L07/L09/L10/L11/L15/L16 正文及 L13 引述的原始 gatekeeper，针对各独立项逐特征比对；L14 网页公式显示疑点按 PDF/代码核对，详解使用自行列明假设的标准高斯式，不直接照抄疑似转换错误。
3. 按中文同义词、分类、申请人和引证继续扩展，并补齐截止日附近未能有效排序的近期专利检索。当前最新性覆盖是有限核验，不是完整查新报告。
4. 按各案第 11 节完成最小闭环原型与反例测试，记录失败、时延、误差界和边界标定，而不只选取成功场景。
5. 核对发明人实际技术贡献、企业权属、首次研发记录及此前对外公开；正式申请前避免公开拟申请方案的新增细节。
6. 由专利代理人与研发共同调整独立项必要特征及从属层级，分别评价可专利性和自由实施，不作授权保证。