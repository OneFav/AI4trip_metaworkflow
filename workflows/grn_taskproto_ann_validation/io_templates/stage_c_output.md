purpose: 输出 Top-K 任务原型匹配结果
required_fields:
  - topk_prototypes
  - distance_summary
optional_fields:
  - parameter_recommendations
example_content: |
  topk_prototypes:
    grn_01:
      - prototype: Proto-Memory
        score: 0.18
      - prototype: Proto-Switch
        score: 0.31
  distance_summary:
    metric: GW
  parameter_recommendations:
    Proto-Memory:
      delay_range: [2, 4]
done_criteria: |
  Top-K 结果与距离摘要可用于 checkpoint 决策。
