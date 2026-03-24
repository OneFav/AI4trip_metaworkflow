# Human-Agent Boundary

## Human does

- 提供 GRN 数据来源、实验/模拟约束与可用注释
- 指定任务原型库版本与可用 probe family 范围
- 决策是否进入 ANN 测试与外部验证阶段
- 审阅最终结论与验证可靠性

## Agent does

- 解析输入并完成 GRN 预处理与模块化
- 编译 probe family 并映射到 GRN 条件
- 构造 GRN/ANN 的 PIRG 并计算距离
- 生成 Top-K 任务原型与 ANN 排序结果
- 产出验证报告草稿与统计摘要

## Human-Agent collaboration

- 在 checkpoint 审阅 Top-K 任务原型与距离证据
- 协同决定验证策略与负对照设置
- 共同解释失败案例与置信度结论

## Trip 场景中的人适合做的事

- 判断实验成本与可行性
- 决定是否采用更严格或更保守的验证标准

## Agent 适合后台推进的事

- 大规模距离计算与排序
- 统一探针测量与批处理验证
