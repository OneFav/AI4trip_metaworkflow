purpose: 输出任务原型库与 prototype PIRG
required_fields:
  - prototype_library_ref
  - prototype_pirg_refs
optional_fields:
  - aggregation_summary
example_content: |
  prototype_library_ref: data/prototypes/v1
  prototype_pirg_refs:
    Proto-Memory: data/prototypes/v1/pirg/proto_memory.pirg
  aggregation_summary:
    strategy: geometric_median
done_criteria: |
  每个任务原型都有可引用的 PIRG 文件。
