# Run Experiment

## experiment_input

* code_path: `<sample_code_path>`
* mode: balanced
* paper_type: cdc_short

## run_command

`/code_to_cdc_short_paper <sample_code_path> --paper-type cdc_short --mode balanced`

## execution_trace_summary

1. stage_1 完成：生成主张-证据矩阵草稿。
2. stage_2 完成：生成严谨性缺口报告与实验计划。
3. Checkpoint A 触发：模拟“批准优先级前 3 项实验”。
4. stage_3 完成：生成结果表与统计摘要模板。
5. stage_4 完成：生成短文草稿模板与图表映射。
6. Checkpoint B 触发：模拟“进入最终稿前需人工压缩篇幅”。

## checkpoint_events

* checkpoint_a: triggered, approved_with_scope_limit
* checkpoint_b: triggered, revision_required

## outputs_generated

* workflow 规范文件齐全
* 关键中间产物路径已定义
* 最终稿路径已定义

## pass_fail_judgement

partial

## issues_and_fixes

1. 问题：未接入真实 LaTeX 模板适配。修复建议：引入 `latex_template_adapter`。
2. 问题：引用质量检查未自动化。修复建议：补充 `bib_quality_checker`。
