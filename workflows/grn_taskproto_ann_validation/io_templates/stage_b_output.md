purpose: 输出 GRN-PIRG 与观测配置摘要
required_fields:
  - grn_pirg_refs
  - observation_summary
optional_fields:
  - mapping_notes
example_content: |
  grn_pirg_refs:
    grn_01: outputs/pirg/grn_01.pirg
  observation_summary:
    level: module
    probes_used: 12
done_criteria: |
  每个 GRN 产生 PIRG 文件并能追溯观测配置。
