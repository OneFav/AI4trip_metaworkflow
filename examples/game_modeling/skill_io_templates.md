# Skill I/O Templates

## Meta

* based_on_plan: workflows/game_modeling/workflow_plan.md
* created_at: 2026-03-18
* status: ready_for_build

## Template Root

* path: `workflows/game_modeling/io_templates/`

## Stage Templates

### Stage 1

* input_template_file: `io_templates/stage_1_input.md`
* output_template_file: `io_templates/stage_1_output.md`
* required_fields:
  * game_name
  * rule_text
  * player_set
* optional_fields:
  * hidden_information_rules
  * time_horizon
* done_criteria: 产出可计算的策略空间、收益定义与约束说明

### Stage 2

* input_template_file: `io_templates/stage_2_input.md`
* output_template_file: `io_templates/stage_2_output.md`
* required_fields:
  * players
  * action_space
  * payoff_definitions
  * transition_rules
* optional_fields:
  * simulation_budget
  * seed_list
* done_criteria: 生成可复现实验日志与策略演化指标汇总

### Stage 3

* input_template_file: `io_templates/stage_3_input.md`
* output_template_file: `io_templates/stage_3_output.md`
* required_fields:
  * simulation_summary
  * parameter_grid
  * observed_equilibrium_candidates
* optional_fields:
  * symbolic_assumptions
  * numerical_tolerance
* done_criteria: 输出均衡解或稳定点分析，并完成与仿真结果的对照

### Stage 4

* input_template_file: `io_templates/stage_4_input.md`
* output_template_file: `io_templates/stage_4_output.md`
* required_fields:
  * solver_results
  * consistency_report
  * assumption_registry
* optional_fields:
  * extension_options
  * unresolved_cases
* done_criteria: 产出最终结论建议与下一轮迭代决策

## Handoff Mapping

### Handoff 1

* from_stage: stage_1
* to_stage: stage_2
* output_to_input_mapping:
  * stage_1_output.players -> stage_2_input.players
  * stage_1_output.action_space -> stage_2_input.action_space
  * stage_1_output.payoff_definitions -> stage_2_input.payoff_definitions
  * stage_1_output.transition_rules -> stage_2_input.transition_rules
* validation_rules:
  * players 数量与 player_set 一致
  * payoff_definitions 可解析
  * transition_rules 不为空

### Handoff 2

* from_stage: stage_2
* to_stage: stage_3
* output_to_input_mapping:
  * stage_2_output.simulation_summary -> stage_3_input.simulation_summary
  * stage_2_output.parameter_grid -> stage_3_input.parameter_grid
  * stage_2_output.equilibrium_candidates -> stage_3_input.observed_equilibrium_candidates
* validation_rules:
  * simulation_summary 包含平均收益与方差
  * parameter_grid 包含边界定义
  * equilibrium_candidates 至少一个

### Handoff 3

* from_stage: stage_3
* to_stage: stage_4
* output_to_input_mapping:
  * stage_3_output.solver_results -> stage_4_input.solver_results
  * stage_3_output.consistency_report -> stage_4_input.consistency_report
  * stage_3_output.assumption_registry -> stage_4_input.assumption_registry
* validation_rules:
  * solver_results 含求解方法说明
  * consistency_report 标明一致与不一致项
  * assumption_registry 可追踪
