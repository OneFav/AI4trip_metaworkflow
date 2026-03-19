# Input Spec

## Required input

* `game_rules.md`：游戏规则、回合流程、玩家目标

## Optional inputs

* `payoff_hypothesis.md`：收益假设与建模偏好
* `simulation_config.yaml`：仿真预算、随机种子、参数网格
* `solver_constraints.md`：解析求解条件或数值精度要求

## Missing input handling

* 缺少收益假设时，默认生成最小可行收益定义并标记待确认
* 缺少仿真配置时，使用 balanced 预设参数并输出可复现实验配置
* 缺少求解约束时，采用默认数值求解并记录精度风险

## Suggested format

* 规则文件按“玩家、行动、回合、终局、计分”结构组织
* 参数配置优先使用 YAML，便于批运行和版本管理
