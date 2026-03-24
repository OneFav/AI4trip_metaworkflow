purpose: 构建固定任务原型库与 prototype PIRG
required_fields:
  - prototype_definitions
  - probe_family_definitions
  - ann_prototype_group_refs
optional_fields:
  - aggregation_strategy
  - prototype_library_version
example_content: |
  prototype_definitions:
    - Proto-Memory
    - Proto-Switch
  probe_family_definitions:
    Proto-Memory:
      delay_range: [1, 5]
  ann_prototype_group_refs:
    Proto-Memory: data/ann_prototypes/memory/
  aggregation_strategy: geometric_median
done_criteria: |
  任务原型库可被引用，且每个原型都有对应的 probe family 与 ANN 原型组。
