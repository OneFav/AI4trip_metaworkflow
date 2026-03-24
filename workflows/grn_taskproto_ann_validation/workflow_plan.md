# Workflow Plan: GRN→任务原型→ANN验证

## 目标

以 GRN 为输入，构建统一 PIRG 表征，匹配固定任务原型库，并对候选 ANN 进行统一测量与距离排序，最后用外部验证检验匹配结论的可信度。

## 阶段划分

### Stage A：任务原型库构建（离线）

**目标**：构建固定任务原型库与其代表性 PIRG。  
**执行者**：Agent  
**产物**：任务原型定义、probe family、prototype PIRG。

### Stage B：GRN 侧自动测量

**目标**：对 GRN 做预处理、条件映射、响应采集并构造 GRN-PIRG。  
**执行者**：Agent  
**产物**：GRN-PIRG 与可追溯的观测配置。

### Stage C：GRN → 任务原型匹配

**目标**：计算 GRN-PIRG 与任务原型 PIRG 的距离，输出 Top-K 任务原型及参数建议。  
**执行者**：Agent  
**产物**：Top-K 任务原型、距离排序、参数范围。

### Stage D：ANN 候选集统一测试

**目标**：对候选 ANN 统一测量并构造 ANN-PIRG，排序与 GRN 的距离。  
**执行者**：Agent  
**产物**：ANN 排序与距离指标。

### Stage E：外部验证与报告

**目标**：验证“距离近 → 更适合该任务原型”的结论可靠性，并形成报告。  
**执行者**：Human-Agent  
**产物**：验证结果、置信度评估、失败案例与报告。

## Checkpoint

在 Stage C 结束后触发 report-decision：  
Agent 输出 Top-K 任务原型与距离证据，Human 决定是否进入 ANN 统一测试与外部验证。

## External Search Verification

### Verified Candidate 1

- capability: GW 距离与最优传输求解
- candidate_skill_or_source: Python Optimal Transport (POT)
- source_url: https://github.com/PythonOT/POT
- why_match: 支持 Gromov-Wasserstein 与多种 OT 变体，直接对齐 Stage C 距离引擎需求

### Verified Candidate 2

- capability: 大规模 OT/GW（JAX 加速）
- candidate_skill_or_source: OTT-JAX
- source_url: https://github.com/ott-jax/ott
- why_match: 支持加速 OT/GW 计算，适配较大规模 PIRG 比对场景

### Verified Candidate 3

- capability: GRN 推断与 regulon 分析
- candidate_skill_or_source: pySCENIC
- source_url: https://github.com/aertslab/pySCENIC
- why_match: 可作为 Stage B 的 GRN 观测与模块化增强工具

### Verified Candidate 4

- capability: 单细胞表达预处理与特征构建
- candidate_skill_or_source: Scanpy
- source_url: https://github.com/scverse/scanpy
- why_match: 可用于 Stage B 的生物侧输入预处理与质量控制

### Verified Candidate 5

- capability: SSM 家族候选模型
- candidate_skill_or_source: Mamba SSM
- source_url: https://github.com/state-spaces/mamba
- why_match: 对齐 Stage D 的 SSM 候选 ANN 测试路径

## External Candidate Integration Plan

### 集成策略

- 采用“本地适配器 + 外部候选库”双层结构
- 本地适配器先落盘为可调用 stub，负责输入校验、调用约定、失败回退
- 外部候选库保持 `candidate_verified_not_installed`，不误标为本地可执行

### 适配映射

- Stage B:
  - scanpy_preprocessor_adapter -> scanpy
  - pyscenic_adapter -> pySCENIC
- Stage C:
  - pot_gw_adapter -> PythonOT/POT
  - ott_jax_gw_adapter -> ott-jax
- Stage D:
  - mamba_ssm_adapter -> mamba

## Inter-Skill I/O Contracts

### Handoff 1

- from_stage: stage_b
- to_stage: stage_c
- handoff_output_template: io_templates/stage_b_output.md
- handoff_input_template: io_templates/stage_c_input.md
- field_mapping:
  - grn_pirg_refs -> grn_pirg_refs
  - observation_summary -> distance_context
- validation_rules:
  - grn_pirg_refs 必须非空
  - distance_metric 必须属于 [GW, Frobenius, rank_correlation]

### Handoff 2

- from_stage: stage_c
- to_stage: stage_d
- handoff_output_template: io_templates/stage_c_output.md
- handoff_input_template: io_templates/stage_d_input.md
- field_mapping:
  - topk_prototypes -> topk_prototypes
  - distance_summary.metric -> ann_distance_metric
- validation_rules:
  - topk_prototypes 至少包含 1 个原型
  - ann_candidates 必须非空
