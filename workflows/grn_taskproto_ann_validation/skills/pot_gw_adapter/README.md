# pot_gw_adapter

role: 对接 PythonOT(POT) 的 GW 距离计算适配层

inputs:
  - source_pirg_ref
  - target_pirg_ref
  - gw_config

outputs:
  - gw_distance
  - transport_plan_ref

constraints:
  - 若 POT 未安装，返回 dependency_missing 并请求切换到 ott_jax_gw_adapter 或简化距离

fallback_policy:
  - 使用 Frobenius 近似距离作为兜底，不进入主验证结论

example:
  input: source_pirg_ref=outputs/pirg/grn_01.pirg, target_pirg_ref=data/prototypes/proto_memory.pirg
  output: gw_distance=0.21
