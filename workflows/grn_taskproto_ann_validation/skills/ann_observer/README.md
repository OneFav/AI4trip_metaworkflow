# ann_observer

role: ANN 状态/激活的统一观测与读出

inputs:
  - ann_model_ref
  - compiled_probes

outputs:
  - ann_response_matrices

constraints:
  - 统一观测层级与采样规则

example:
  input: gru_model + memory probes
  output: outputs/response/ann_gru_matrix.npy
