# ann_runner

role: 候选 ANN 训练/加载并统一测量

inputs:
  - ann_candidates
  - training_policy
  - compiled_probes

outputs:
  - trained_ann_refs
  - training_summary

constraints:
  - 训练不足时标记为不可比较样本

example:
  input: gru, sparse_mlp
  output: outputs/ann/gru.pt
