# mamba_ssm_adapter

role: 对接 mamba-ssm 的 SSM 候选模型训练/评估适配层

inputs:
  - task_prototype_config
  - training_profile
  - probe_family_ref

outputs:
  - mamba_checkpoint_ref
  - ann_pirg_ref
  - training_metrics_ref

constraints:
  - 若 mamba-ssm 未安装，返回 candidate_unavailable 并退出该候选分支

fallback_policy:
  - 保留 GRU/SSM 其他候选分支继续执行

example:
  input: task_prototype_config=configs/proto_memory.yaml
  output: mamba_checkpoint_ref=outputs/ann/mamba_proto_memory.pt
