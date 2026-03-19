# Intent

## Meta

* workflow_name: game_modeling
* created_at: 2026-03-18
* status: intent_defined

## Goal

将一个桌游或游戏规则转化为可分析的博弈模型，完成数学建模、Python 沙盘演化仿真与数学求解，并输出可复用的结论与参数敏感性洞察。

## Scene

该 workflow 主要用于 research + desk 场景，适用于策略分析、机制设计验证和教学演示。核心计算在桌面端完成，移动端可用于查看报告与做阶段决策。

## Design Intent

该 workflow 的价值在于把“直觉策略讨论”变成“可计算、可复现实验、可解释结论”的闭环。它先抽象规则与收益结构，再通过仿真和解析求解相互校验，避免只停留在口头策略判断。

## Human-Agent Boundary

### Human

* 定义目标游戏、规则边界与建模假设
* 决定是否采用完全信息/不完全信息、静态/动态博弈框架
* 审核结论解释与现实含义，决定最终采用的模型版本

### Agent

* 将规则形式化为状态、行动、收益与转移关系
* 生成 Python 沙盘仿真脚本并执行批量实验
* 进行参数扫描、均衡候选计算与结果可视化汇总

### Human-Agent

* 共同确定关键假设是否合理
* 在 checkpoint 评估“仿真结果与数学解是否一致”
* 决策后续是扩展模型复杂度还是收敛到当前版本

## Candidate Checkpoints

1. 建模冻结点：在完成规则形式化后，agent 停止并汇报状态空间、策略空间、收益定义；human 决定是否批准进入仿真与求解。
2. 结论发布点：在得到仿真与数学解后，agent 汇报一致性、敏感性和异常案例；human 决定是否发布结论或回退修模。

## Automation Preference

* mode: balanced
* reason: 形式化、仿真与批量计算可高自动化，但建模假设与结论解释必须保留人类主导。

## Trip/Mobile Orientation

* trip_compatible: partial
* mobile_friendly: partial
* notes: 计算密集任务依赖桌面端；移动端适合查看阶段报告、批准 checkpoint 和做参数微调指令。

## Notes for Skill 2

后续流程设计应优先保证“规则抽象一致性 -> 仿真可复现 -> 解析求解可对照”三段闭环，不要先堆算法；必须把模型假设、变量定义、求解条件写成可校验的 I/O 模板字段。
