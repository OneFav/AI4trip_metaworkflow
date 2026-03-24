# ott_jax_gw_adapter

role: 对接 OTT-JAX 的加速 GW/OT 计算适配层

inputs:
  - source_pirg_ref
  - target_pirg_ref
  - jax_runtime_profile

outputs:
  - gw_distance
  - solver_log_ref

constraints:
  - 需要 JAX 运行环境，若不可用则降级到 pot_gw_adapter

fallback_policy:
  - 自动切换 pot_gw_adapter
  - 若 POT 也不可用，降级到 distance_engine 的近似模式

example:
  input: source_pirg_ref=outputs/pirg/grn_01.pirg
  output: solver_log_ref=outputs/logs/ott_jax_grn_01.json
