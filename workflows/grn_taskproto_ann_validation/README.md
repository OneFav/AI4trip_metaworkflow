# GRN→任务原型→ANN验证 工作流

## 这是一个什么 workflow

将 GRN 与 ANN 统一映射为 PIRG，并在固定任务原型库内完成匹配与验证，产出 Top-K 假设与外部验证报告。

## 适合场景

- 需要将 GRN 的计算结构与任务原型建立可比较的映射
- 需要在固定任务原型库中筛选最可能匹配的任务

## 谁做什么

- Human：提供 GRN 数据与实验约束，确认是否进入验证阶段
- Agent：完成 PIRG 构造、距离排序与验证报告草稿

## 怎么调用

```text
/grn_taskproto_ann_validation <input_file> --top_k 3
```

## 当前局限

- 依赖 GRN 与 ANN 的可观测数据质量
- 验证结论仍需要真实实验支撑
