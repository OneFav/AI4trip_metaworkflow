purpose: GRN 预处理、条件映射与响应采集
required_fields:
  - grn_items
  - grn_observation_level
  - prototype_library_ref
optional_fields:
  - condition_mapping_overrides
  - simulation_policy
example_content: |
  grn_items:
    - id: grn_01
      source: data/grn/grn_01.json
  grn_observation_level: module
  prototype_library_ref: data/prototypes/v1
  simulation_policy: simulate_if_missing
done_criteria: |
  每个 GRN 都有可追溯的观测层级与条件映射配置。
