purpose: 外部验证与报告生成
required_fields:
  - topk_prototypes
  - ann_rankings
  - validation_policy
optional_fields:
  - control_settings
example_content: |
  topk_prototypes:
    grn_01: [Proto-Memory]
  ann_rankings:
    grn_01:
      Proto-Memory:
        - ann: gru
          score: 0.20
  validation_policy:
    correlation: true
    rank_consistency: true
    ablation: true
done_criteria: |
  生成验证结论与置信度报告。
