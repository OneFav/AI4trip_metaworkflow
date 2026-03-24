# Skill IO Templates

## Stage A: 任务原型库构建

- input_template: io_templates/stage_a_input.md
- output_template: io_templates/stage_a_output.md

## Stage B: GRN 侧自动测量

- input_template: io_templates/stage_b_input.md
- output_template: io_templates/stage_b_output.md

## Stage C: GRN→任务原型匹配

- input_template: io_templates/stage_c_input.md
- output_template: io_templates/stage_c_output.md

## Stage D: ANN 候选集统一测试

- input_template: io_templates/stage_d_input.md
- output_template: io_templates/stage_d_output.md

## Stage E: 外部验证与报告

- input_template: io_templates/stage_e_input.md
- output_template: io_templates/stage_e_output.md

## 字段映射与最小校验

- Stage A 输出的 prototype_library_ref 必须出现在 Stage B/C/D 的输入中
- Stage B 输出的 grn_pirg_refs 必须出现在 Stage C 的输入中
- Stage C 输出的 topk_prototypes 必须出现在 Stage D/E 的输入中
- Stage D 输出的 ann_rankings 必须出现在 Stage E 的输入中
