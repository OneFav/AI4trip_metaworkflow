# distance_engine

role: 计算 PIRG 间距离并排序

inputs:
  - grn_pirg_refs
  - prototype_pirg_refs
  - distance_metric

outputs:
  - distance_matrices
  - ranking_summary

constraints:
  - 默认主距离使用 GW

example:
  input: grn_01.pirg vs proto_memory.pirg, metric=GW
  output: outputs/distances/grn_01_topk.json
