# Skill I/O Templates

## Stage Template Mapping

* stage_1_input: `io_templates/stage1_input.md`
* stage_1_output: `io_templates/stage1_output.md`
* stage_2_input: `io_templates/stage2_input.md`
* stage_2_output: `io_templates/stage2_output.md`
* stage_3_input: `io_templates/stage3_input.md`
* stage_3_output: `io_templates/stage3_output.md`
* stage_4_input: `io_templates/stage4_input.md`
* stage_4_output: `io_templates/stage4_output.md`
* stage_5_input: `io_templates/stage5_input.md`
* stage_5_output: `io_templates/stage5_output.md`

## Field Mapping

1. `stage1_output.claim_matrix` -> `stage2_input.claim_matrix`
2. `stage2_output.approved_experiments` -> `stage3_input.experiment_plan`
3. `stage3_output.key_tables` -> `stage4_input.evidence_tables`
4. `stage3_output.figure_index` -> `stage4_input.figure_index`
5. `stage4_output.draft_text` -> `stage5_input.draft_text`
6. `stage4_output.citation_needs` -> `stage5_input.citation_review`

## Minimal Validation Rules

1. stage_1 输出必须包含至少 1 个核心主张与对应证据定位。
2. stage_2 输出必须包含优先级排序与资源预算。
3. stage_3 输出必须包含统计项定义与至少一项结果表。
4. stage_4 输出必须包含摘要、方法、结果、结论四个核心模块。
5. stage_5 输出必须包含投稿检查清单与最终交付路径。
