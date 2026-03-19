---
name: "consistency_checker"
description: "检查仿真结果与数学求解结论的一致性。对比沙盘演化与均衡计算的策略分布。当需要验证仿真与理论解是否匹配时调用。"
---

# Consistency Checker

## Implementation Logic

1.  **Result Alignment**:
    *   加载 `stage_2_output.json` (仿真摘要) 与 `stage_3_output.json` (数学解)。
2.  **Comparison Rules**:
    *   比较 `strategies` 分布的 `Mean Squared Error` (MSE)。
    *   比较 `avg_payoffs` 是否在 `tolerance` 范围内一致。
    *   比较 `equilibrium_candidates` 是否属于数学解集中的任一均衡。
3.  **Discrepancy Attribution**:
    *   若不一致，检查 `simulation_budget` 是否过小。
    *   检查是否存在 `local_optima`。
    *   检查 `numerical_tolerance` 是否冲突。
4.  **Integration**:
    *   输出 `consistency_report.json` (一致性判断、偏差列表、置信等级)。

## Dependencies
- `json`
- `numpy`

## Usage
```bash
python main.py stage_2_output.json stage_3_output.json
```
