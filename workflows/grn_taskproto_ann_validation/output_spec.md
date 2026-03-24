# Output Spec

## 预期输出文件

### 中间产物

- prototype_pirg_bundle/：任务原型 PIRG 集合
- grn_pirg/：每个 GRN 的 PIRG
- ann_pirg/：每个候选 ANN 的 PIRG
- distance_matrices/：距离矩阵与中间统计

### 最终交付物

- topk_task_prototypes.json：每个 GRN 的 Top-K 任务原型匹配
- ranked_ann_results.json：ANN 距离排序与指标
- validation_report.md：外部验证结果与置信度结论

## 面向对象

- 给人看的输出：validation_report.md、topk_task_prototypes.json 摘要
- 给后续流程的输出：PIRG 与距离矩阵、排序结果
