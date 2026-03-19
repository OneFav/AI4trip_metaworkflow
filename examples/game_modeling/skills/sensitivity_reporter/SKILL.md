---
name: "sensitivity_reporter"
description: "输出参数敏感性与阈值变化报告。基于博弈求解结果分析参数扰动对均衡的影响。当需要结论的鲁棒性评估时调用。"
---

# Sensitivity Reporter

## Implementation Logic

1.  **Parameter Scanning**:
    *   加载 `stage_3_output.json` (数学解)。
    *   按照 `parameter_grid` 执行收益参数的小幅扰动。
2.  **Sensitivity Calculation**:
    *   计算均衡策略对各个收益项的偏导数 (Jacobian Matrix)。
    *   识别 `Critical Thresholds` (即均衡类型发生改变的参数临界值)。
3.  **Report Formatting**:
    *   将敏感参数列表按重要性排序。
    *   汇总 `Robustness Range` (在该范围内均衡解保持拓扑一致)。
4.  **Integration**:
    *   输出 `sensitivity_report.json` (敏感性结论、阈值备注、鲁棒性指标)。

## Dependencies
- `numpy`
- `matplotlib` (可选, 用于敏感性热力图)

## Usage
```bash
python main.py stage_3_output.json
```
