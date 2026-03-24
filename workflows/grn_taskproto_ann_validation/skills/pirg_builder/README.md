# pirg_builder

role: 将响应矩阵构造为 PIRG

inputs:
  - response_matrices
  - similarity_metric

outputs:
  - pirg_refs

constraints:
  - 默认使用 probe-probe 相似度矩阵

example:
  input: response_matrix.npy, similarity=cosine
  output: outputs/pirg/grn_01.pirg
