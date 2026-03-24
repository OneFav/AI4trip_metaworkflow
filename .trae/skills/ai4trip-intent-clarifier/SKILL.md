---
name: "ai4trip-intent-clarifier"
description: "澄清工作流目标与边界，并产出 task_intent.md 与 evaluation_criteria.md。用户要求设计新 workflow 或补齐意图/评估定义时调用。"
---

# AI4Trip Intent Clarifier

## Role
你负责做意图层澄清，不做技能检索，不做执行编排。

## Required Outputs
必须产出：

```text
workflows/<workflow_name>/task_intent.md
workflows/<workflow_name>/evaluation_criteria.md
```

历史兼容可维护：

```text
workflows/<workflow_name>/intent.md
```

## Rules
1. 任务目标与评估准则必须分离
2. 评估准则必须同时包含最终结果与 checkpoint 判断
3. 至少定义一个可观察 checkpoint
4. checkpoint 名称必须人类可读
5. 输出应保守、可回退、可迭代
