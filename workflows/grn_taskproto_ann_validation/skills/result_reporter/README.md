# result_reporter

role: 汇总输出报告与置信度结论

inputs:
  - topk_prototypes
  - ann_rankings
  - validation_metrics

outputs:
  - validation_report_ref
  - confidence_summary

constraints:
  - 报告必须包含失败案例与负对照结果

example:
  input: topk_prototypes + validation_metrics
  output: outputs/reports/validation_report.md
