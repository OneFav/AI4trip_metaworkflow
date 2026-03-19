---
name: "python_sandbox_simulator"
description: "执行 Python 沙盘仿真。基于 Mesa 框架构建博弈演化环境并执行批量对局。当形式化模型建立且需要验证演化路径时调用。"
---

# Python Sandbox Simulator

## Implementation Logic

1.  **Environment Setup**: 
    *   使用 `Mesa` 初始化 `GameModel` 类。
    *   根据 `stage_1_output.json` 初始化玩家 `Agents` 与收益矩阵。
2.  **Simulation Loop**:
    *   按照 `RandomActivation` 或 `StagedActivation` 驱动对局。
    *   在每一步中记录各玩家的行动选择与瞬时收益。
3.  **Data Aggregation**:
    *   对 `simulation_budget` 内的所有对局进行均值与方差统计。
    *   识别出现频率最高的策略组合作为 `equilibrium_candidates`。
4.  **Integration**:
    *   输出 `stage_2_output.json` (统计摘要、候选均衡、收敛日志)。

## Dependencies
- `mesa`
- `numpy`
- `pandas`

## Usage
```bash
python main.py stage_2_input.json
```
