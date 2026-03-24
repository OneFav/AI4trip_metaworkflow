# validator

role: 验证距离排序与任务适配性的关系

inputs:
  - ann_rankings
  - validation_policy
  - control_settings

outputs:
  - validation_metrics
  - failure_cases

constraints:
  - 必须包含至少一种负对照

example:
  input: rank_consistency=true, ablation=true
  output: outputs/validation/summary.json
