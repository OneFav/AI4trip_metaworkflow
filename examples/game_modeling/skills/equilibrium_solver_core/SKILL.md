---
name: "equilibrium_solver_core"
description: "执行博弈均衡求解与稳定性分析。使用 Nashpy 或 Gambit 求解 Nash 均衡。当需要数学解析解来对照仿真结果时调用。"
---

# Equilibrium Solver Core

## Implementation Logic

1.  **Model Loading**: 接收 `stage_1_output.json` 中的 `payoff_matrix`。
2.  **Algorithm Selection**:
    *   2人博弈: 使用 `Nashpy` (Lemke-Howson, Support Enumeration)。
    *   N人博弈: 使用 `Gambit` (Simplicial Decomposition) 或 `OpenSpiel` 的均衡求解器。
3.  **Numerical Solving**:
    *   计算 `Pure Strategy Nash Equilibria` (PSNE)。
    *   计算 `Mixed Strategy Nash Equilibria` (MSNE)。
    *   评估解的稳定性 (Evolutionary Stability)。
4.  **Integration**:
    *   输出 `stage_3_output.json` (含解集、精度参数、假设依赖)。

## Dependencies
- `nashpy`
- `gambit` (可选, 针对多玩家)
- `scipy.optimize`

## Usage
```bash
python main.py stage_3_input.json
```
