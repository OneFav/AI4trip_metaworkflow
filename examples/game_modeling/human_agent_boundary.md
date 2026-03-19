# Human-Agent Boundary

## Human does

* 给出原始游戏规则、建模目标与评价口径
* 冻结关键建模假设并批准是否进入仿真阶段
* 审核求解结论外推范围并决定是否发布结论

## Agent does

* 将规则结构化为状态、行动、收益与转移定义
* 生成并运行 Python 沙盘仿真与参数扫描
* 执行均衡求解、稳定性分析与一致性报告汇总

## Human-Agent collaboration

* 在 checkpoint_model_freeze 共同确认形式化模型是否忠实原规则
* 在 checkpoint_consistency_gate 共同评估仿真与数学解偏差
* 共同决定继续迭代还是收敛到当前模型版本

## Trip notes

* 规则讨论、假设选择、结果解释适合 Human 主导
* 批量仿真与求解可由 Agent 后台推进
