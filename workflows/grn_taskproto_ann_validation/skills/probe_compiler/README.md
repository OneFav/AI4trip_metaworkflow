# probe_compiler

role: 统一 probe family 并映射到 GRN/ANN 条件

inputs:
  - probe_family_definitions
  - condition_mapping_overrides

outputs:
  - compiled_probes
  - mapping_summary

constraints:
  - 条件语义同构，不要求物理输入一致

example:
  input: Memory.delay_range -> GRN sampling window
  output: compiled_probes/memory.yaml
