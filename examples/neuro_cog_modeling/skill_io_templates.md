# Skill I/O Templates

## Meta

* based_on_plan: workflows/neuro_cog_modeling/workflow_plan.md
* created_at: 2026-03-18
* status: ready_for_build

## Template Root

* path: `workflows/neuro_cog_modeling/io_templates/`

## Stage Templates

### Stage 1

* input_template_file: `io_templates/stage_1_input.md`
* output_template_file: `io_templates/stage_1_output.md`
* required_fields:
  * phenomena_1_description
  * phenomena_2_description
  * data_source_or_summary
* optional_fields:
  * known_theories
* done_criteria: 文献调研报告包含至少 5 篇核心文献，并梳理出关键矛盾点。

### Stage 2

* input_template_file: `io_templates/stage_2_input.md`
* output_template_file: `io_templates/stage_2_output.md`
* required_fields:
  * literature_review_summary
  * target_phenomena
* optional_fields:
  * preferred_framework (DDM/RL/PyMC)
* done_criteria: 提出至少 2 个具有数学形式的候选模型。

### Stage 3

* input_template_file: `io_templates/stage_3_input.md`
* output_template_file: `io_templates/stage_3_output.md`
* required_fields:
  * selected_model
  * challenge_cases (3 scenarios)
* optional_fields:
  * biological_constraints
* done_criteria: 针对每个质疑场景，模型给出了合理的定性或定量回应。

### Stage 4

* input_template_file: `io_templates/stage_4_input.md`
* output_template_file: `io_templates/stage_4_output.md`
* required_fields:
  * defended_model_structure
  * empirical_data_path
* optional_fields:
  * fitting_parameters (MCMC samples, etc.)
* done_criteria: 完成数据拟合，输出参数后验分布与拟合优度指标。

### Stage 5

* input_template_file: `io_templates/stage_5_input.md`
* output_template_file: `io_templates/stage_5_output.md`
* required_fields:
  * fitting_results
  * interpretation_goals
* optional_fields:
  * publication_target
* done_criteria: 生成包含图表与理论讨论的完整报告。

## Handoff Mapping

### Handoff 1

* from_stage: stage_1
* to_stage: stage_2
* output_to_input_mapping:
  * literature_summary -> literature_review_summary
  * key_conflicts -> constraints
* validation_rules:
  * literature_summary 不得为空。

### Handoff 2

* from_stage: stage_2
* to_stage: stage_3
* output_to_input_mapping:
  * best_candidate_model -> selected_model
  * model_assumptions -> defense_basis
* validation_rules:
  * selected_model 必须包含公式描述。

### Handoff 3

* from_stage: stage_3
* to_stage: stage_4
* output_to_input_mapping:
  * refined_model_structure -> defended_model_structure
  * confirmed_constraints -> priors
* validation_rules:
  * refined_model_structure 必须反映对质疑的回应。

### Handoff 4

* from_stage: stage_4
* to_stage: stage_5
* output_to_input_mapping:
  * fit_statistics -> fitting_results
  * parameter_posteriors -> parameter_interpretation_base
* validation_rules:
  * fit_statistics 必须包含 AIC 或 BIC。
