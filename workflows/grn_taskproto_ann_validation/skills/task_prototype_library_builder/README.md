# task_prototype_library_builder

role: 构建固定任务原型库并生成 prototype PIRG

inputs:
  - prototype_definitions
  - probe_family_definitions
  - ann_prototype_group_refs

outputs:
  - prototype_library_ref
  - prototype_pirg_refs

constraints:
  - 任务原型必须来自固定库，不做开放世界生成

example:
  input: Proto-Memory, Proto-Switch
  output: data/prototypes/v1/pirg/proto_memory.pirg
