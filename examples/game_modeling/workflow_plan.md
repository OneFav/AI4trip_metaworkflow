# Workflow Plan

## Meta

* based_on_intent: workflows/game_modeling/intent.md
* created_at: 2026-03-18
* status: ready_for_build

## Suggested Workflow Type

custom

## Workflow Stages

### Stage 1

* name: 规则抽象与博弈形式化
* goal: 将桌游规则转为参与者、策略、状态、收益与约束的数学定义
* executor: Human-Agent
* required_capabilities:
  * rule_parsing
  * game_formalization
  * assumption_registry
* input_template_file: io_templates/stage_1_input.md
* output_template_file: io_templates/stage_1_output.md

### Stage 2

* name: Python沙盘构建与演化仿真
* goal: 基于形式化模型实现仿真器并执行参数扫描、策略演化与对局批运行
* executor: Agent
* required_capabilities:
  * simulation_coding
  * batch_experiment
  * metrics_logging
* input_template_file: io_templates/stage_2_input.md
* output_template_file: io_templates/stage_2_output.md

### Stage 3

* name: 数学求解与均衡分析
* goal: 用解析方法或数值方法求解均衡、稳定性与关键阈值，并与仿真结果对照
* executor: Agent
* required_capabilities:
  * equilibrium_solver
  * symbolic_or_numeric_analysis
  * consistency_check
* input_template_file: io_templates/stage_3_input.md
* output_template_file: io_templates/stage_3_output.md

### Stage 4

* name: 结论收敛与模型修订决策
* goal: 汇总建模、仿真和求解证据，决定模型是否收敛或继续迭代
* executor: Human-Agent
* required_capabilities:
  * report_generation
  * discrepancy_diagnosis
  * decision_support
* input_template_file: io_templates/stage_4_input.md
* output_template_file: io_templates/stage_4_output.md

## Guidebook Matches

### Match 1

* capability: simulation_coding
* candidate_skill_or_source: guides/skill_registry.md -> entry_003 (Claude Code Skills Collection)
* why_match: 适合工程化脚本组织、阶段化执行与质量门控

### Match 2

* capability: experiment_cycle_design
* candidate_skill_or_source: guides/skill_registry.md -> entry_005 (AutoRA)
* why_match: 可借鉴“实验设计-执行-评估”循环结构

### Match 3

* capability: research_iteration
* candidate_skill_or_source: guides/skill_registry.md -> entry_001 (ARIS)
* why_match: 可借鉴“自动执行 + 复盘”框架组织建模与验证迭代

## External Search Verification

### Verified Candidate 1

* capability: game_environment_modeling + multi-agent simulation
* candidate_skill_or_source: OpenSpiel (google-deepmind/open_spiel)
* why_match: 覆盖多类博弈范式并提供 Python 接口，适合“规则到环境”的标准化建模
* reliability_signal:
  * 项目公开维护且有 release 信息
  * 官方定位明确为 games 中的 RL 与 search/planning 研究框架
* adoption_risk:
  * 学习曲线较高
  * 与纯 Python 轻量脚本相比集成成本更高

### Verified Candidate 2

* capability: equilibrium_computation (pure/mixed Nash)
* candidate_skill_or_source: Gambit (gambitproject/gambit)
* why_match: 专门面向非合作博弈计算，适合 stage_3 的均衡求解主通道
* reliability_signal:
  * 官方项目定位明确为 game theory computation
  * 长期项目并有独立项目站点
* adoption_risk:
  * 工具链与安装配置可能高于纯 Python 包

### Verified Candidate 3

* capability: two-player game solving and teaching-friendly equilibrium routines
* candidate_skill_or_source: Nashpy (drvinceknight/Nashpy)
* why_match: 对 2 人矩阵博弈求解直接可用，可作为 stage_3 快速求解路径
* reliability_signal:
  * 文档与教程完善，PyPI 可安装
  * 生态中与 Gambit 形成互补
* adoption_risk:
  * 主要面向 2 人博弈，不覆盖一般 n-player 全场景

### Verified Candidate 4

* capability: agent-based sandbox evolution
* candidate_skill_or_source: Mesa (mesa/mesa)
* why_match: 适合构建可视化与可复现的 Python 沙盘演化实验
* reliability_signal:
  * 文档显示持续维护并有近期稳定版/预发布版
  * 有明确的安装与版本迁移说明
* adoption_risk:
  * 偏 ABM 抽象，不直接提供博弈均衡求解

### Verified Candidate 5

* capability: repeated game tournament and strategy dynamics
* candidate_skill_or_source: Axelrod-Python/Axelrod
* why_match: 对重复博弈与策略演化研究成熟，可补强 stage_2 演化实验
* reliability_signal:
  * 明确的研究工具定位与成熟策略库
  * 历史项目活跃且文档完整
* adoption_risk:
  * 聚焦 IPD 类问题，不是通用博弈建模框架

### Verified Candidate 6

* capability: multi-agent environment API standardization
* candidate_skill_or_source: PettingZoo (Farama-Foundation/PettingZoo)
* why_match: 可作为复杂多智能体环境接口层，便于统一训练/评估循环
* reliability_signal:
  * 明确 API 标准定位与版本化策略
  * 近期 release 仍在更新
* adoption_risk:
  * 更偏 MARL 环境封装，不等同于博弈论解析求解器

## Workflow Reframing Notes

* 当前 workflow 的问题：如果直接“先写求解器”，容易跳过规则抽象一致性校验，导致后续仿真与数学分析语义不一致。
* 建议如何重划：先将“规则形式化”独立成 stage_1，再分别执行仿真与求解，最后集中做一致性决策。
* 哪些步骤应拆开：仿真执行与数学求解应拆开，便于单独定位偏差来源。
* 哪些步骤应合并：结论解释与是否继续迭代的决策应合并在 stage_4。
* 哪些步骤应从 agent 自动化中拿回给人：模型假设冻结与最终结论外推必须由人主导。

## Human-Agent Boundary

### Human

* 决定建模范围、关键假设与目标问题
* 决定对现实规则的抽象简化是否可接受
* 决定最终模型版本与输出结论口径

### Agent

* 自动生成并运行仿真代码
* 自动执行参数扫描与批量记录
* 自动做均衡候选求解与一致性对照

### Human-Agent

* 共同确认形式化定义是否忠实于原游戏规则
* 共同判断仿真-求解偏差是否可解释
* 共同决定是否进入下一轮迭代

## Candidate Checkpoints

1. checkpoint_model_freeze：stage_1 后触发，agent 汇报变量、约束、收益函数；human 决定是否批准进入仿真与求解。
2. checkpoint_consistency_gate：stage_3 后触发，agent 汇报仿真与数学解一致性；human 决定是否发布结论或回退修模。

## Remaining Gaps

* guides/workflow_patterns.md 当前缺失，workflow pattern 只能基于 skill_registry 与 skill_sources 推断。
* 若目标是一般 n-player 复杂动态博弈，仍需补充“统一求解编排层”，将 OpenSpiel/Gambit/Nashpy 的能力按问题类型路由。
* 若要直接支持移动端轻量交互，需要在后续 Build 阶段增加“远程运行 + 结果摘要回传”接口设计。

## Inter-Skill I/O Contracts

### Handoff 1

* from_stage: stage_1
* to_stage: stage_2
* handoff_output_template: io_templates/stage_1_output.md
* handoff_input_template: io_templates/stage_2_input.md
* field_mapping:
  * players -> simulator.players
  * action_space -> simulator.action_space
  * payoff_definitions -> simulator.payoff_function
  * transition_rules -> simulator.state_transition
* validation_rules:
  * players 非空
  * action_space 对每个玩家均定义
  * payoff_definitions 含可计算表达

### Handoff 2

* from_stage: stage_2
* to_stage: stage_3
* handoff_output_template: io_templates/stage_2_output.md
* handoff_input_template: io_templates/stage_3_input.md
* field_mapping:
  * simulation_summary -> solver.empirical_targets
  * parameter_grid -> solver.parameter_domain
  * observed_equilibrium_candidates -> solver.initial_points
* validation_rules:
  * simulation_summary 包含关键指标统计
  * parameter_grid 至少包含一组可复现实验参数

## I/O Template File Plan

* template_root: `workflows/game_modeling/io_templates/`
* files_to_create:
  * `stage_1_input.md`
  * `stage_1_output.md`
  * `stage_2_input.md`
  * `stage_2_output.md`
  * `stage_3_input.md`
  * `stage_3_output.md`
  * `stage_4_input.md`
  * `stage_4_output.md`
* each_template_must_include:
  * purpose
  * required_fields
  * optional_fields
  * example_content
  * done_criteria

## Recommendation

* next_skill: workflow_builder
* reason: 阶段结构、checkpoint 和 I/O 合同已完整，可进入构建落盘阶段。
