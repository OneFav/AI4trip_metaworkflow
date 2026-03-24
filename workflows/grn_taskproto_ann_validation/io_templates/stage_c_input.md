purpose: GRN→任务原型匹配
required_fields:
  - grn_pirg_refs
  - prototype_pirg_refs
  - distance_metric
optional_fields:
  - top_k
example_content: |
  grn_pirg_refs:
    grn_01: outputs/pirg/grn_01.pirg
  prototype_pirg_refs:
    Proto-Memory: data/prototypes/v1/pirg/proto_memory.pirg
  distance_metric: GW
  top_k: 3
done_criteria: |
  产生每个 GRN 的 Top-K 任务原型与距离排序结果。
