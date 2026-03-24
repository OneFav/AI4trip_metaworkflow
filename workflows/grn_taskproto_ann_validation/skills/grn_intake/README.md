# grn_intake

role: 读取 GRN 数据并标准化为统一 schema

inputs:
  - grn_items
  - grn_observation_level

outputs:
  - normalized_grn_refs
  - observation_summary

constraints:
  - 不直接使用全基因表达，优先 module/regulon 层级

example:
  input: grn_items=[grn_01], grn_observation_level=module
  output: normalized_grn_refs={grn_01: outputs/grn/grn_01.norm}
