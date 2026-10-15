# 导航规划控制专利组合与文献检索台账

> 检索基准日：2026-10-15。
> 交付版本：V1.1；三篇完整交底书，完成两轮文献驱动收敛与技术修订。
> 证据范围：10 篇核心论文、7 件核心专利；论文中 4 篇核读方法正文，6 篇核读摘要；7 件专利均核读书目及相关权利要求。
> 性质：研发与代理沟通草案，非授权、新颖性或自由实施法律意见。
> 适用对象：具备转向、驱动和制动接口的自动驾驶车辆；不推定仓库已有实车实现。

## 1. 交付目录与阅读顺序

| 案件 | 完整交底书 | 拟保护的技术链路 | 近期直接对比 |
| --- | --- | --- | --- |
| A | [01_patent_a_occlusion_handover_certificate_disclosure_20261015.md](01_patent_a_occlusion_handover_certificate_disclosure_20261015.md) | 接管时延过渡状态管、备份可接管集合、主轨迹前缀放行证书与控制侧接管 | L01 版本更新至 2026-10-05；P01、P02、P07 |
| B | [02_patent_b_friction_evidence_consistent_planning_disclosure_20261015.md](02_patent_b_friction_evidence_consistent_planning_disclosure_20261015.md) | 分轮附着证据适用域、轮轨迹段约束依赖、失效传播、同版本规划分配执行 | L05、L09 均为 2026 论文；P06 为 2026 授权专利 |
| C | [03_patent_c_local_frame_route_handover_disclosure_20261015.md](03_patent_c_local_frame_route_handover_disclosure_20261015.md) | 地图失配后连续局部控制、出口假设共同前缀、不可逆分叉停止约束与重验回切 | L03、L08、L10；P05 为 2026 授权专利 |

每篇均含 12 个一级章节：摘要、现有技术、问题、最小技术组合、模块接口、实施步骤、数值实施例、附图、区别与风险、权利要求建议、验证计划、迭代及补证。每案附两幅 Mermaid 示意图。摘要和权利要求为建议稿，不是正式申请文件。

建议先读各案第 4、9、12 节确定保护边界，再由研发核对第 6、7、11 节的可实现性。发明人、申请人、首次形成时间、车型和 ECU 参数必须按真实记录补入。

## 2. 检索范围与最新性边界

使用 arXiv 公告时间倒序检索、摘要页版本历史、可访问论文 HTML 正文、Google Patents 检索索引和公开全文。近期线索优先覆盖 2025-2026 年，但保留能直接削弱宽泛创新主张的早期基础文献。

本轮实际核验的近期更新包括：L01 v3（2026-10-05）、L04 首稿（2026-10-02）、L10 v2（2026-10-02）、L05 首稿（2026-07-11），以及 P05 授权公告（2026-04-07）、P06 授权公告（2026-02-06）。论文首稿、修订、期刊出版和专利申请公布、授权公告分别记录，不混作同一种“发表时间”。

不声称这些是全球最新的全部成果，也不声称三案具有已被法律确认的新颖性。未公开申请、数据库延迟、非英语/中文文献、全文不可检索附件、同族差异和检索语义遗漏均可能影响结论。CNIPA、WIPO、Espacenet、USPTO 的官方档案与审查意见尚未逐件复核。

访问与过滤限制：

- Google 通用搜索抓取无有效正文，浏览器访问一度超时；Bing 返回页面框架但无有效结果，不作为完成检索的证据。
- Google Patents 正文抓取部分返回 503，P04-P06 后通过浏览器取得有效书目及权利要求。
- 末轮尝试 `after=publication:20250101`、`before=publication:20261016`、`sort=new` 的结构化检索，返回记录包含 2015、2018 年专利，日期筛选和排序未得到验证。该轮只作为过滤失败记录，不能据此认定“2026 年 10 月前最新专利已查全”。
- 各核心来源中的日期均由具体摘要页或全文书目核对，不以检索排序代替日期验证；L04 索引曾显示 10 月 1 日，原始提交历史为 10 月 2 日，本台账采用后者。

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

arXiv 按公告时间排序主要反映首版公告年月，不保证最近修订优先；因此必须单独读取已有强相关论文的版本历史。

后续官方检索建议结合 B60W60/00、B60W30/09、B60W40/06、G05D1/00、G01C21/00 等分类及“备份接管、执行前缀、分轮附着、约束撤销、定位失配、出口歧义”等中文同义词，继续做申请人、同族和引证扩展。分类为建议入口，未完成全部分类检索。

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

## 6. 反例驱动的收敛与实际修订

| 案件 | 首轮宽泛设想与反例 | 初稿 V1.0 的收敛 | 第二轮新增证据及实际 V1.1 修订 |
| --- | --- | --- | --- |
| A | 遮挡感知、双轨迹和共享前缀已由 L01 披露；反应时间与过期验证见 P01/P02 | 接管过渡管包含于未来备份可接管集合，反算主轨迹可执行前缀 | 核读 P07 后增加“时延未异常但接管已不可达”的对照，纠正 B1/B2；补齐整个停止时域覆盖和统计时延保证边界 |
| B | 附着不确定性 MPC 见 L07；自然激励、分轮动作及置信度衰减见 P03 | 附着证据适用域与轮轨迹段依赖撤销、同版本规划分配执行 | 核读 P06 权利要求后删除附着场、前后轴分配和控制器同步的首创暗示；依据 L09 补输入耦合重验；补指令代际、生效时刻和队列撤销过渡 |
| C | 感知导航与不确定性传播见 L03/L08；地图差异见 P04；横纵限制见 P05 | 合理出口假设共同前缀、不可逆分叉停止边界、连续局部接管与重验回切 | 核读 L10 摘要后将多假设和延迟提交归为已有方向；加入出口提交撤销、相关重复误匹配及完整停止时域误差增长约束 |

## 7. 技术假设、保护分工与风险

| 案件 | 待检验机制 | 能推翻假设的证据或测试 |
| --- | --- | --- |
| A | 备份未来可接管集合限制主轨迹放行前缀，而非分别检查两条轨迹 | 单一在先文献完整公开同一关系；或接管过渡段在允许界内仍错误放行 |
| B | 局部附着证据撤销经轮轨迹段依赖改变速度、力分配和确认生效时刻 | 相同依赖传播在先完整披露；或附着突降时仍跨版本执行或忽略已排队输入 |
| C | 多出口共同前缀决定局部接管及不可逆分叉前停止，而非只选择最高分出口 | 在先公开相同链路；或出口未消歧仍越界、局部误差增长后才停车 |

三案可分别实施：A 不要求使用 B 的附着估计器，底盘能力可来自既有接口；B 不要求遮挡或地图失配；C 不要求 A 的证书格式或 B 的证据图。联合部署时可交换保守底盘能力和有效走廊，但独立权利要求不应互相依赖才具备完整实施链路。

优先建议：按目标研发资源选择 B 的约束失配闭环或 A 的接管监控作为最小原型；C 依赖局部定位完整性、道路拓扑与规则验证，集成门槛更高。这是实施工作量排序，不是授权概率排序。

三案均存在较强的创造性组合风险：可达性监督、依赖传播、版本一致性、假设树与局部坐标本身均非新概念。当前不能据“未在已读来源找到全部组合”宣布具有专利法上的新颖性或创造性；需要单篇对照新颖性分析、最接近文献及结合动机分析，和官方同族权利要求的自由实施评估。

## 8. 已做检查与未做验证

已逐案执行首次写入检查与 V1.1 修订回归：

| 案件 | 复算项目 | 结果与含义 |
| --- | --- | --- |
| A | 8 m/s、0.20 s 接管、3 m/s² 保证减速、1.5 m 裕量 | 停止所需 13.767 m；14 m 可用距离下最多等待约 0.029 s；接管增至 0.30 s 后需 14.567 m，应拒绝原放行 |
| B | 单轮载荷 4000 N、附着下界 0.25、裕量 0.8、横向需求 500 N | 纵向力上限 624.5 N；错误采用 0.70 则得到 2183.5 N；降至 0.15 后横向需求本身已不可行 |
| B | 20 m 内将速度降至 8 m/s，保证减速 2 m/s² | 忽略时延的上游筛查上界 12 m/s，当前 15 m/s 时不能靠修改目标速度宣称可行 |
| C | 9 m 分叉前停止、0.25 s 时延、2 m/s² 减速、误差及裕量合计 1 m | 速度筛查上界 5.179 m/s；5 m/s 需 8.5 m；6 m/s 需 11.5 m，不能承诺在原边界前停住 |
| C | 3.6 m 走廊、1.9 m 车宽、0.25 m 误差、0.20 m 裕量 | 中心轨迹每侧余量 0.40 m；误差增至 0.70 m 时余量 -0.05 m，拒绝继续依赖原走廊 |

另检查 12 节结构、围栏闭合、来源编号映射、本地链接和三案诊断；通过只表示文档完整性及示例算术一致。编辑器对三案未报告诊断错误，不代表公式证明或专利质量认证。Mermaid 为流程源图，未进行专门渲染器预览。

未做：完整算法实现、求解器测试、统计显著性测试、车辆动力学仿真、硬件在环、实车标定、安全认证、专业查新或侵权评价。各案验证计划可作为后续研发实验清单，不能把计划中的样本数或效果写成既有结果。

## 9. 申请前的必要补证

1. 从官方数据库下载核心专利公布/授权原文及审查档案，核对同族、申请主体和真实优先权链；特别关注 P01/P06 的主体差异。
2. 补读仅摘要核验的 L02/L04/L06/L07/L09/L10 正文，针对每案独立项做逐特征比对，而非只比较摘要用词。
3. 按中文同义词、分类、申请人和引证继续扩展，并补齐截止日附近未能有效排序的近期专利检索。当前最新性覆盖是有限核验，不是完整查新报告。
4. 按各案第 11 节完成最小闭环原型与反例测试，记录失败、时延、误差界和边界标定，而不只选取成功场景。
5. 核对发明人实际技术贡献、企业权属、首次研发记录及此前对外公开；正式申请前避免公开拟申请方案的新增细节。
6. 由专利代理人与研发共同调整独立项必要特征及从属层级，分别评价可专利性和自由实施，不作授权保证。