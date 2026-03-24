# Skills Manifest

| skill_name | status | source | local_path | version_or_commit | license | notes |
| --- | --- | --- | --- | --- | --- | --- |
| grn_intake | created_local_stub | local_stub | workflows/grn_taskproto_ann_validation/skills/grn_intake | local_stub_v0 | N/A | 读取 GRN 数据并标准化 schema |
| task_prototype_library_builder | created_local_stub | local_stub | workflows/grn_taskproto_ann_validation/skills/task_prototype_library_builder | local_stub_v0 | N/A | 构建固定任务原型库与 prototype PIRG |
| probe_compiler | created_local_stub | local_stub | workflows/grn_taskproto_ann_validation/skills/probe_compiler | local_stub_v0 | N/A | 统一 probe family 与条件映射 |
| grn_observer | created_local_stub | local_stub | workflows/grn_taskproto_ann_validation/skills/grn_observer | local_stub_v0 | N/A | GRN 侧观测与响应采集 |
| ann_observer | created_local_stub | local_stub | workflows/grn_taskproto_ann_validation/skills/ann_observer | local_stub_v0 | N/A | ANN 侧观测与状态读出 |
| ann_runner | created_local_stub | local_stub | workflows/grn_taskproto_ann_validation/skills/ann_runner | local_stub_v0 | N/A | 候选 ANN 训练/加载与统一测量 |
| pirg_builder | created_local_stub | local_stub | workflows/grn_taskproto_ann_validation/skills/pirg_builder | local_stub_v0 | N/A | 构造 PIRG 表征 |
| distance_engine | created_local_stub | local_stub | workflows/grn_taskproto_ann_validation/skills/distance_engine | local_stub_v0 | N/A | 计算 PIRG 距离与排序 |
| validator | created_local_stub | local_stub | workflows/grn_taskproto_ann_validation/skills/validator | local_stub_v0 | N/A | 外部验证与负对照 |
| result_reporter | created_local_stub | local_stub | workflows/grn_taskproto_ann_validation/skills/result_reporter | local_stub_v0 | N/A | 报告与置信度输出 |
| scanpy_preprocessor_adapter | created_local_stub | local_wrapper | workflows/grn_taskproto_ann_validation/skills/scanpy_preprocessor_adapter | local_stub_v0 | N/A | scanpy 预处理适配层，负责依赖检测与回退 |
| pyscenic_adapter | created_local_stub | local_wrapper | workflows/grn_taskproto_ann_validation/skills/pyscenic_adapter | local_stub_v0 | N/A | pySCENIC 推断适配层，负责依赖检测与回退 |
| pot_gw_adapter | created_local_stub | local_wrapper | workflows/grn_taskproto_ann_validation/skills/pot_gw_adapter | local_stub_v0 | N/A | POT GW 适配层，支持不可用时降级 |
| ott_jax_gw_adapter | created_local_stub | local_wrapper | workflows/grn_taskproto_ann_validation/skills/ott_jax_gw_adapter | local_stub_v0 | N/A | OTT-JAX GW 适配层，支持切换 POT |
| mamba_ssm_adapter | created_local_stub | local_wrapper | workflows/grn_taskproto_ann_validation/skills/mamba_ssm_adapter | local_stub_v0 | N/A | mamba-ssm 候选训练适配层 |
| python_optimal_transport_pot | downloaded | https://github.com/PythonOT/POT | workflows/grn_taskproto_ann_validation/external_candidates/POT | 41a4d57 | MIT | 已下载到本地快照，未接入环境安装 |
| ott_jax | downloaded | https://github.com/ott-jax/ott | workflows/grn_taskproto_ann_validation/external_candidates/ott-jax | e7d02d0 | Apache-2.0 | 已下载到本地快照，未接入环境安装 |
| pySCENIC | downloaded | https://github.com/aertslab/pySCENIC | workflows/grn_taskproto_ann_validation/external_candidates/pySCENIC | 06bafba | GPL-3.0 | 已下载到本地快照，未接入环境安装 |
| scanpy | downloaded_partial | https://github.com/scverse/scanpy | workflows/grn_taskproto_ann_validation/external_candidates/scanpy | 9de11b1 | BSD-3-Clause | Windows 路径长度导致部分测试资源未checkout |
| mamba_ssm | downloaded | https://github.com/state-spaces/mamba | workflows/grn_taskproto_ann_validation/external_candidates/mamba | ee2a86a | Apache-2.0 | 已下载到本地快照，未接入环境安装 |
| gene2ai-openclaw-skill | downloaded | clawhub:gene2ai-openclaw-skill | workflows/grn_taskproto_ann_validation/skills/gene2ai-openclaw-skill | 0.1.5 | MIT-0 | 已通过 clawhub install 下载，SKILL.md 可直接调用 |
| flow-cytometry-gating-strategist | downloaded_with_risk_warning | clawhub:flow-cytometry-gating-strategist | workflows/grn_taskproto_ann_validation/skills/flow-cytometry-gating-strategist | 0.1.0 | MIT-0 | 安装时收到 VirusTotal suspicious 警告，已仅落盘并待人工审计后启用 |
