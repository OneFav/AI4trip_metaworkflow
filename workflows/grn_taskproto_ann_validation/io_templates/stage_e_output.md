purpose: 输出验证报告与可信度结论
required_fields:
  - validation_report_ref
  - confidence_summary
optional_fields:
  - failure_cases
example_content: |
  validation_report_ref: outputs/reports/validation_report.md
  confidence_summary:
    grn_01: moderate
  failure_cases:
    - grn_01: shuffled_grn_control_failed
done_criteria: |
  产生可追溯的验证报告与可信度摘要。
