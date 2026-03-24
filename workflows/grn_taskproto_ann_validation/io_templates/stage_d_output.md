purpose: 输出 ANN 距离排序与 ANN-PIRG 引用
required_fields:
  - ann_rankings
  - ann_pirg_refs
optional_fields:
  - training_summary
example_content: |
  ann_rankings:
    grn_01:
      Proto-Memory:
        - ann: gru
          score: 0.20
  ann_pirg_refs:
    gru: outputs/pirg/ann_gru.pirg
done_criteria: |
  产生 ANN 排序与可引用的 ANN-PIRG 文件。
