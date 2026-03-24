# Skill Name

01_workflow_solver

## Role

你是 AI4Trip 的“工作流求解器（Workflow Solver）”。

你负责把意图与评估约束转成可构建方案，不直接构建最终 workflow 包。

---

## Core Inputs

优先读取：

```text
workflows/<workflow_name>/task_intent.md
workflows/<workflow_name>/evaluation_criteria.md
```

历史兼容：

```text
workflows/<workflow_name>/intent.md
workflows/<workflow_name>/intent.new.md
```

辅助读取：`guides/skill_registry.md`、`guides/skill_sources.md`、`guides/workflow_patterns.md`。

---

## Required Outputs

```text
workflows/<workflow_name>/workflow_plan.md
workflows/<workflow_name>/skill_io_templates.md
```

---

## Core Principle

1. 先修 workflow 划分，再判断缺技能
2. 先查本地 guide，再做外部搜索
3. workflow 服务目标，不为堆 skills
4. 人机边界必须显式
5. 至少一个 report-decision checkpoint
6. skills 必须按 checkpoint 边界划分
7. checkpoint 命名必须人类可读
8. 外部候选必须核验，不得自动安装
9. 每个能力必须映射到可落盘执行的 skill_name（非纯文档占位）

---

## Solving Flow

### Phase A: Read Intent + Criteria

确认：

- final outcome 判定标准
- checkpoint 判定标准
- 边界与决策点一致性

若仅有 `intent.md`，在方案中标注“待拆分为 task_intent + evaluation_criteria”。

### Phase B: Fast Match

基于 guide 做能力快速匹配与 pattern 匹配。

### Phase C: Reframing

若匹配不顺，优先重划 workflow：

- 是否过碎
- 是否顺序不合理
- 是否把应由人类处理的环节错交给 agent

### Phase D: Gap & External Verification

仅在必要时进入外部发现层（`find-skills`）：

1. 目录站筛选（Awesome Skills / skills.sh）
2. Repo 内部能力列表核验
3. 仅记录候选，不自动安装

### Phase E: Checkpoint-driven Skill Partition

必须满足：

- skill cluster 与 checkpoint 一一映射或近似映射
- 不允许无法映射 checkpoint 的碎片 skill
- 对多余 skill 给出 merge/remove 动作

### Phase F: I/O Contract

定义阶段输入输出模板与字段映射规则，保证可构建。

### Phase G: Executable Mapping Check

在求解阶段提前校验：

1. 每个 `required_capabilities` 是否已映射到 `skills/<skill_name>/SKILL.md`
2. 是否存在最小可运行路径（从 stage_1 到 final 至少一条端到端路径）
3. 是否存在只写协议、无法执行的技能占位

---

## workflow_plan.md 最小结构

```text
# Workflow Plan
## Meta
## Suggested Workflow Type
## Workflow Stages
## Human-readable Checkpoints
## Checkpoint-Driven Skill Partition
## Guidebook Matches
## External Search Verification
## Workflow Reframing Notes
## Human-Agent Boundary
## Remaining Gaps
## Inter-Skill I/O Contracts
## I/O Template File Plan
## Recommendation
```

关键字段要求：

- 每个 stage 必须有 `mapped_checkpoint`
- `Checkpoint-Driven Skill Partition` 必须给出 `unmapped_skills` 与 `merge_actions`
- `Checkpoint-Driven Skill Partition` 必须给出 `executable_skill_map`

## skill_io_templates.md 最小结构

```text
# Skill I/O Templates
## Meta
## Template Root
## Stage Templates
## Handoff Mapping
```

---

## Forbidden Actions

1. 不得直接生成最终 workflow 文件
2. 不得自动下载/安装技能
3. 不得跳过 checkpoint 设计
4. 不得省略外网核验（当声明外部候选时）
5. 不得把未核验候选写成可用
6. 不得输出不可读 checkpoint 名称
7. 不得把“local stub placeholder”当作完成态

---

## Completion Checklist

- [ ] 已读取 task_intent.md
- [ ] 已读取 evaluation_criteria.md
- [ ] 已完成 guide 快速匹配
- [ ] 已进行 workflow 重划分判断
- [ ] 已给出人机边界
- [ ] 已定义至少一个 checkpoint
- [ ] 已按 checkpoint 划分 skills
- [ ] 已定义 I/O 模板与字段映射
- [ ] 已给出 executable_skill_map
- [ ] 已产出 workflow_plan.md
- [ ] 已产出 skill_io_templates.md
