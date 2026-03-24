# grn_observer

role: GRN 条件响应采集与观测

inputs:
  - normalized_grn_refs
  - compiled_probes

outputs:
  - grn_response_matrices

constraints:
  - 缺少真实数据时允许使用模拟响应

example:
  input: grn_01 + memory probes
  output: outputs/response/grn_01_matrix.npy
