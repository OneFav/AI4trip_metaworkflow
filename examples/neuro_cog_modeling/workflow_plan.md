# Workflow Plan

## Meta

* based_on_intent: workflows/neuro_cog_modeling/intent.md
* created_at: 2026-03-18
* status: ready_for_build

## Suggested Workflow Type

research_from_zero

## Workflow Stages

### Stage 1

* name: 文献调研与理论梳理
* goal: 针对用户提出的两个现象，梳理现有理论解释、关键参数与潜在矛盾，建立知识库。
* executor: Agent
* required_capabilities:
  * literature-reviewer-skill (from claw.club)
  * academic-research (local snapshot under workflows/neuro_cog_modeling/skills/)
  * local_literature_search (fallback)
  * theoretical_synthesis
  * parameter_extraction
* input_template_file: io_templates/stage_1_input.md
* output_template_file: io_templates/stage_1_output.md

### Stage 2

* name: 模型假设提出与框架选择
* goal: 基于调研结果，提出 2-3 个能统合两个现象的数学模型候选（如 DDM, RL, 贝叶斯等），并阐述其生物学/心理学合理性。
* executor: Agent
* required_capabilities:
  * mathematical_modeling
  * hypothesis_generation
  * framework_selection (HDDM, PyMC, RL)
* input_template_file: io_templates/stage_2_input.md
* output_template_file: io_templates/stage_2_output.md

### Stage 3

* name: 质疑-辩护循环 (Challenge-Response Loop)
* goal: 人类提出反例场景，Agent 尝试调整模型结构或参数以回应质疑，验证模型的鲁棒性与边界。
* executor: Human-Agent
* required_capabilities:
  * counterfactual_reasoning
  * model_adjustment
  * critical_dialogue
* input_template_file: io_templates/stage_3_input.md
* output_template_file: io_templates/stage_3_output.md

### Stage 4

* name: 模型编码与数据拟合
* goal: 编写选定模型的 Python 代码（集成 HDDM/PyMC/Stable-Baselines3），执行参数搜索与实证数据拟合，计算 AIC/BIC。
* executor: Agent
* required_capabilities:
  * Jupyter MCP Server (交互式沙盒)
  * python_coding (PyMC/HDDM)
  * optimization
  * statistical_inference
* input_template_file: io_templates/stage_4_input.md
* output_template_file: io_templates/stage_4_output.md

### Stage 5

* name: 拟合评估与最终报告
* goal: 评估拟合优度，解释参数的心理学/生物学含义，生成最终的统一建模报告。
* executor: Human-Agent
* required_capabilities:
  * result_interpretation
  * report_generation
  * plotly-data-visualization (MCP Skill)
* input_template_file: io_templates/stage_5_input.md
* output_template_file: io_templates/stage_5_output.md

## Guidebook Matches

### Match 1

* capability: research_iteration
* candidate_skill_or_source: guides/skill_registry.md -> entry_001 (ARIS)
* why_match: ARIS 的 "review-loop" 模式非常适合 Stage 3 的质疑-辩护循环。

### Match 2

* capability: empirical_workflow_patterns
* candidate_skill_or_source: guides/skill_registry.md -> entry_005 (AutoRA)
* why_match: AutoRA 的 "model discovery" 理念与 Stage 2 的模型假设提出高度一致。

## External Search Verification

### Directory & Repo Scan Result

* 目录站查询 (claw.club / skills.sh / MCP Market)：成功发现专门用于文献调研的打包 Agent Skill（支持多数据库与中文工作流）。
* 针对核心的认知神经科学数学建模部分，目前仍需将成熟的 Python 认知建模库（HDDM / PyMC）作为外部能力来源，并在本工作流中构建 Agent Wrapper。

### Verified Candidate 1 (Literature Review Skill)

* capability: 系统性中英文献回顾（8阶段工作流），跨数据库文献查找
* candidate_project: literature-reviewer-skill / literature-search
* source_url: claw.club (ClawHub)
* install_command: 依托 claw.club/MCP 生态安装
* action: 已通过 `clawhub inspect --file --json` 拉取可复现快照到 `workflows/neuro_cog_modeling/skills/academic-research/`，规避安装限流问题。

### Verified Candidate 2 (Jupyter MCP Server)

* capability: 提供本地 Jupyter Notebook 的双向通信，允许 Agent 直接编写、执行代码（包括 PyMC/HDDM 拟合代码），并获取文本输出与可视化图像。
* candidate_project: Jupyter MCP Server (例如 `jjsantos01/jupyter-notebook-mcp`)
* source_url: MCP Market / GitHub
* verification_summary: 完美契合 Stage 4（模型编码与数据拟合）与 Stage 5（结果评估），使 Agent 能在一个交互式的沙盒中进行参数寻优和绘制后验分布图，而不需要每次都手写独立的 Python 脚本。
* action: 推荐在 Stage 4 中作为默认的代码执行沙盒环境。

### Verified Candidate 3 (Plotly Data Visualization)

* capability: 生成复杂的科学可视化图表（支持 3D 表面、分布图、热力图等），支持多格式导出。
* candidate_project: plotly-data-visualization (Claude Code Skill)
* source_url: mcpmarket.com
* verification_summary: 适用于 Stage 5，用于可视化 HDDM 的漂移率分布或后验预测检查（Posterior Predictive Checks）。
* action: DO NOT INSTALL YET. Write to plan.

### Verified Candidate 4 (Python Library / 核心依赖)

* capability: hierarchical drift diffusion modeling (DDM)
* candidate_project: HDDM (hddm-devs/hddm)
* source_url: https://github.com/hddm-devs/hddm
* verification_summary: 专门用于认知神经科学与心理学的分层贝叶斯漂移扩散模型（基于 PyMC）。
* integration_recommendation: 结合上述 Jupyter MCP Server 运行，不再需要从零手写硬编码的 `hddm_model_fitter` wrapper。
* risks: 依赖特定的 Python 环境（如 `pymc==2.3.8` 或老版本），安装配置可能存在环境冲突。

### Verified Candidate 2 (Python Library Wrapper)

* capability: General Bayesian Cognitive Modeling
* candidate_project: PyMC (pymc-devs/pymc)
* source_url: https://github.com/pymc-devs/pymc
* verification_summary: 通用的概率编程框架，可用于实现除 DDM 以外的任意认知模型。
* maintenance_signal: 高度活跃，社区强大。
* license: Apache-2.0
* integration_recommendation: 作为 HDDM 的底层或作为构建自定义贝叶斯模型的替代引擎。同样需要构建本地 Wrapper。
* risks: 编写自定义模型的 Agent 失败率较高，需要极强的统计建模知识。

## Workflow Reframing Notes

* 当前 workflow 的问题: 传统的“建模-拟合”流程容易忽视理论的边界条件。
* 建议如何重划: 显式引入 Stage 3 (Challenge-Response Loop) 作为独立阶段，而不仅仅是一个 Checkpoint。
* 哪些步骤应拆开: 模型提出 (Stage 2) 与 代码实现 (Stage 4) 应拆开，中间插入质疑环节。
* 哪些步骤应合并: 拟合执行与参数搜索合并在 Stage 4。
* 哪些步骤应从 agent 自动化中拿回给人: 反例的提出 (Stage 3 Input) 与最终的模型生物学合理性评估 (Stage 5)。

## Human-Agent Boundary

### Human

* 提出两个现象与相关数据 (Stage 1 Input)。
* 选定模型框架 (Checkpoint 1)。
* 提出反例质疑 (Stage 3 Input)。
* 评估最终报告 (Stage 5)。

### Agent

* 文献调研与理论梳理 (Stage 1)。
* 模型假设生成 (Stage 2)。
* 针对反例的模型修正 (Stage 3)。
* 代码编写与数据拟合 (Stage 4)。
* 报告生成 (Stage 5)。

### Human-Agent

* 质疑-辩护对话 (Stage 3)。
* 结果解释与下一步计划 (Stage 5)。

## Candidate Checkpoints

1. checkpoint_model_proposal: Stage 2 结束后，Human 选择模型框架。
2. checkpoint_challenge_response: Stage 3 结束后，Human 确认模型已充分回应质疑。
3. checkpoint_fit_evaluation: Stage 4 结束后，Human 评估拟合优度。

## Remaining Gaps

* 缺乏专门针对“认知模型拟合”（如参数恢复性测试）的现成 Skill，需要基于 PyMC/HDDM 编写 Wrapper。
* “文献调研”能力依赖于外部搜索 API 的质量，可能需要多轮迭代。

## Inter-Skill I/O Contracts

### Handoff 1

* from_stage: stage_1
* to_stage: stage_2
* handoff_output_template: io_templates/stage_1_output.md
* handoff_input_template: io_templates/stage_2_input.md
* field_mapping:
  * key_phenomena -> target_phenomena
  * theoretical_constraints -> constraints
* validation_rules:
  * theoretical_constraints 必须包含至少 3 条关键约束。

### Handoff 2

* from_stage: stage_2
* to_stage: stage_3
* handoff_output_template: io_templates/stage_2_output.md
* handoff_input_template: io_templates/stage_3_input.md
* field_mapping:
  * candidate_models -> target_model
  * biological_plausibility -> defense_basis
* validation_rules:
  * candidate_models 必须包含数学形式化描述。

## I/O Template File Plan

* template_root: `workflows/neuro_cog_modeling/io_templates/`
* files_to_create:
  * `stage_1_input.md`
  * `stage_1_output.md`
  * `stage_2_input.md`
  * `stage_2_output.md`
  * `stage_3_input.md`
  * `stage_3_output.md`
  * `stage_4_input.md`
  * `stage_4_output.md`
  * `stage_5_input.md`
  * `stage_5_output.md`
* each_template_must_include:
  * purpose
  * required_fields
  * optional_fields
  * example_content
  * done_criteria

## Recommendation

* next_skill: workflow_builder
* reason: 方案已包含文献调研、质疑循环与外部技能核验，结构完整，可进入构建。
