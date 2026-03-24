# scanpy_preprocessor_adapter

role: 对接 scanpy 的单细胞预处理适配层

inputs:
  - expression_matrix_ref
  - preprocessing_profile

outputs:
  - normalized_expression_ref
  - qc_summary

constraints:
  - 若 scanpy 未安装，返回标准化失败状态并触发本地回退流程

fallback_policy:
  - 使用本地简化预处理流程（log1p + zscore）并标记为 surrogate

example:
  input: expression_matrix_ref=data/grn/sc_expr.h5ad
  output: normalized_expression_ref=outputs/grn/sc_expr.norm.h5ad
