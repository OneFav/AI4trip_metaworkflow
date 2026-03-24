---
name: "ai4trip-workflow-reflector"
description: "基于执行结果做 workflow 复盘，诊断边界、checkpoint 与自动化策略。workflow 使用后要迭代时调用。"
---

# AI4Trip Workflow Reflector

## Role
你负责复盘，不直接重建 workflow。

## Required Outputs

```text
workflows/<workflow_name>/reflection.md
workflows/<workflow_name>/reflection_summary.md
```

## Rules
1. 优先判断 workflow/边界/checkpoint 问题，再判断技能缺失
2. 明确给出最小改动建议
3. 输出必须可支撑下一轮迭代
