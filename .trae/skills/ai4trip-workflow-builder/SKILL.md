---
name: "ai4trip-workflow-builder"
description: "将 workflow_plan.md 物化为可执行 workflow 包，并记录实验与评估日志。进入构建阶段时调用。"
---

# AI4Trip Workflow Builder

## Role
你负责把方案转成可调用工作流包，并做最小验证。
你产出的 workflow 必须默认“可执行优先”，不能只停留在协议层。

## Required Inputs

```text
workflows/<workflow_name>/workflow_plan.md
workflows/<workflow_name>/skill_io_templates.md
workflows/<workflow_name>/task_intent.md
workflows/<workflow_name>/evaluation_criteria.md
```

## Required Outputs

```text
workflows/<workflow_name>/workflow.yaml
workflows/<workflow_name>/approval_points.md
workflows/<workflow_name>/human_agent_boundary.md
workflows/<workflow_name>/input_spec.md
workflows/<workflow_name>/output_spec.md
workflows/<workflow_name>/command.md
workflows/<workflow_name>/io_templates/
workflows/<workflow_name>/generated/skills_manifest.md
workflows/<workflow_name>/generated/tuning_report.md
workflows/<workflow_name>/generated/run_experiment.md
workflows/<workflow_name>/generated/evaluation_log.md
```

## Executable Skill Requirements

对 `workflow.yaml.dependencies.local_skills` 中每个本地技能，必须满足：

1. 存在 `workflows/<workflow_name>/skills/<skill_name>/SKILL.md`
2. `SKILL.md` 至少包含：
   - `name` 与 `description`
   - `Trigger`（何时调用）
   - `Input Contract`（字段与最小校验）
   - `Execution Steps`（可执行步骤）
   - `Output Contract`（结构化输出）
   - `Failure & Fallback`（失败回退）
3. 若技能依赖外部库，必须提供本地 adapter/wrapper 的降级路径
4. 不允许仅保留 `local stub placeholder` 文本

## Skills Manifest Status Rules

`generated/skills_manifest.md` 中状态必须使用以下之一：

- `integration_ready`：本地可调用，已具备可执行 SKILL.md
- `executable_stub`：有可执行骨架，可跑最小路径
- `unresolved`：仅候选，尚不可本地调用
- `downloaded_not_integrated`：已下载但未接入运行路径

禁止使用“created_local_stub”作为最终验收状态。

## Rules
1. 必须区分 checkpoint 评估与最终结果评估
2. 评估结论必须附证据引用
3. 不得把外部来源误写为本地可用
4. 每个 Agent 阶段至少映射一个可执行技能
5. `command.md` 必须给出可直接执行的标准用法与最小示例
6. `generated/run_experiment.md` 必须包含一次端到端 dry-run 记录
