# pyscenic_adapter

role: 对接 pySCENIC 的 GRN 推断与 regulon 导出适配层

inputs:
  - normalized_expression_ref
  - tf_list_ref
  - scenic_config

outputs:
  - regulon_activity_ref
  - grn_adjacency_ref

constraints:
  - 若 pySCENIC 未安装，仅输出空壳索引并标记 unavailable_dependency

fallback_policy:
  - 回退到已有 GRN 模块输入，不触发自动推断

example:
  input: normalized_expression_ref=outputs/grn/sc_expr.norm.h5ad
  output: regulon_activity_ref=outputs/grn/regulon_activity.csv
