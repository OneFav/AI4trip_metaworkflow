purpose: ANN 候选集统一测试
required_fields:
  - ann_candidates
  - topk_prototypes
  - probe_family_refs
optional_fields:
  - training_policy
example_content: |
  ann_candidates:
    - sparse_mlp
    - gru
  topk_prototypes:
    grn_01: [Proto-Memory, Proto-Switch]
  probe_family_refs:
    Proto-Memory: data/prototypes/v1/probes/memory.yaml
done_criteria: |
  候选 ANN 可被统一测量并产生 ANN-PIRG。
