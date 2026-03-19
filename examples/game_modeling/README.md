# game_modeling

从桌游/游戏规则出发，完成博弈模型数学建模、Python 沙盘演化仿真与数学求解，并输出一致性结论。

## 适用场景

* 策略分析
* 机制设计验证
* 教学与研究演示

## 人机分工

* Human：建模边界、假设冻结、结论解释与发布
* Agent：规则形式化、仿真执行、求解分析、报告汇总
* Human-Agent：checkpoint 决策与偏差诊断

## 调用方式

`/game_modeling game_rules.md --mode balanced`

## 当前局限

* 外部候选能力已核验但默认未安装
* n-player 复杂动态博弈仍需统一求解编排层
