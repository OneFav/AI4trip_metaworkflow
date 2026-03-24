---
name: "ai4trip-workflow-solver"
description: "读取 task_intent.md 与 evaluation_criteria.md，输出 workflow_plan.md 和 skill_io_templates.md。需要按 checkpoint 划分 skills 时调用。"
---

# AI4Trip Workflow Solver

## Role
你负责 workflow 求解，不直接构建最终包。

## Inputs
优先读取：

```text
workflows/<workflow_name>/task_intent.md
workflows/<workflow_name>/evaluation_criteria.md
```

兼容读取：

```text
workflows/<workflow_name>/intent.md
```

## Outputs

```text
workflows/<workflow_name>/workflow_plan.md
workflows/<workflow_name>/skill_io_templates.md
```

## Executable-First Planning

在求解阶段就要保证后续可执行：

1. 每个 `required_capabilities` 必须映射到明确 `skill_name`
2. 每个 `skill_name` 必须能落到 `skills/<skill_name>/SKILL.md`
3. `skill_io_templates.md` 需要包含可直接执行的 I/O 字段与示例
4. 必须给出最小可运行路径（minimal runnable path）

## Rules
1. skills 仅按 checkpoint 边界划分
2. 不得生成无法映射 checkpoint 的碎片 skills
3. checkpoint 命名必须面向人类可读
4. 若存在能力缺口，先重划 workflow 再判断缺 skill
5. 不得把“协议说明”当作“可执行技能”本身
