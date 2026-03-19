# Workflow Plan: story_world

## Meta

* based_on_intent: workflows/story_world/intent.md
* created_at: 2026-03-19
* status: ready_for_build

---

## Suggested Workflow Type

**Custom: Story-to-Sandbox Generation Pipeline**

---

## Workflow Stages

### Stage 1: 实体与意图抽取 (Entity & Intent Extraction)

* **goal**: 从故事文本中抽取实体清单、推断核心意图与主题基调
* **executor**: Agent
* **required_capabilities**:
    * 自然语言理解（实体识别、关系抽取）
    * 主题/基调推断能力
* **input_template_file**: `io_templates/stage1_input_story.md`
* **output_template_file**: `io_templates/stage1_output_entities.md`
* **checkpoint**: Yes（实体对齐，人类审批后进入下一阶段）

---

### Stage 2: 世界规则推断 (World Rule Inference)

* **goal**: 从故事中推断世界规则（物理规则、社会规则），生成规则建议清单
* **executor**: Agent（提案）→ Human（审批）
* **required_capabilities**:
    * 规则归纳与推理能力
    * 现实主义约束校验（仅限现实元素）
* **input_template_file**: `io_templates/stage2_input_entities.md`
* **output_template_file**: `io_templates/stage2_output_rules.md`
* **checkpoint**: Yes（规则校验，人类审批后进入下一阶段）

---

### Stage 3: 关系与行为建模 (Relationship & Behavior Modeling)

* **goal**: 基于实体和规则，建模角色关系网络与每个 Agent 的行为决策树
* **executor**: Agent
* **required_capabilities**:
    * 关系图谱构建
    * 决策树/状态机设计
* **input_template_file**: `io_templates/stage3_input_rules.md`
* **output_template_file**: `io_templates/stage3_output_model.md`
* **checkpoint**: Yes（意图归档，人类审批后进入代码生成）

---

### Stage 4: 沙盘代码生成 (Sandbox Code Generation)

* **goal**: 将模型转化为可运行的 Mesa 多智能体沙盘代码
* **executor**: Agent
* **required_capabilities**:
    * Mesa 框架代码生成
    * Python 代码编写能力
* **input_template_file**: `io_templates/stage4_input_model.md`
* **output_template_file**: `sandbox.py`（输出到 `worlds/<world_name>/`）

---

### Stage 5: 沙盘验证与调优 (Sandbox Verification & Tuning)

* **goal**: 运行沙盘代码，验证输出是否符合故事意图，提出调优建议
* **executor**: Agent
* **required_capabilities**:
    * 代码执行与调试
    * 参数调优能力
* **input_template_file**: `sandbox.py`
* **output_template_file**: `tuning_report.md`

---

## Human / Agent / Human-Agent 边界分配

| 阶段 | 执行者 | 边界类型 |
|------|--------|----------|
| Stage 1 | Agent | A（自动执行）|
| Checkpoint 1 | Human | H（审批实体清单）|
| Stage 2 | Agent → Human | C（Agent提案，H审批）|
| Checkpoint 2 | Human | H（审批规则）|
| Stage 3 | Agent | A |
| Checkpoint 3 | Human | H（审批意图归档）|
| Stage 4 | Agent | A |
| Stage 5 | Agent | A |

---

## Checkpoint 设计

| Checkpoint | 位置 | 审批内容 | 通过标准 |
|------------|------|----------|----------|
| CP1 | Stage 1 → Stage 2 | 实体清单 | 人类确认实体完整且正确 |
| CP2 | Stage 2 → Stage 3 | 世界规则建议 | 人类确认规则符合现实主义约束 |
| CP3 | Stage 3 → Stage 4 | 意图分析报告 | 人类确认模型符合故事精神 |

---

## Guidebook Matches

### Match 1

* capability: 多智能体沙盘框架
* candidate_skill_or_source: **Mesa** (https://github.com/projectmesa/mesa)
* why_match: Mesa 是 Python 生态中最成熟的离散事件多智能体框架，支持 GridSpace/ContinuousSpace，具备可视化服务器，适合生成可运行沙盘

### Match 2

* capability: 自然语言实体抽取
* candidate_skill_or_source: **LLM 内在能力**（GPT-4 / Claude 等大模型内置的 NER + 关系抽取）
* why_match: 无需外部技能，现有大模型已具备高质量实体识别与关系推断能力

### Match 3

* capability: 代码生成
* candidate_skill_or_source: **LLM 内在能力**（大模型代码生成）
* why_match: 现已有多款 LLM 可生成高质量 Python 代码，可直接用于 Mesa 代码生成

---

## External Search Verification

### 已核验候选

| 能力 | 候选来源 | 核验结果 |
|------|----------|----------|
| 多智能体框架 | Mesa | ✅ 可用，pip install mesa 即可 |
| 实体抽取 | LLM 内在能力 | ✅ 首选，无需外部工具 |
| 代码生成 | LLM 内在能力 | ✅ 首选，无需外部工具 |

### 结论

当前 workflow 所需的核心能力（Mesa 框架 + LLM 内在能力）已足够支撑**故事→沙盘**的完整转换，无需引入额外的外部技能包。

---

## Remaining Gaps

暂无明显能力缺口。Stage 5 的调优如果需要更精细的参数搜索，可后续引入 Optuna 等调参库作为可选项。

---

## I/O 字段映射

| 阶段 | 关键输出字段 | 传递给下一阶段的字段 |
|------|-------------|---------------------|
| Stage 1 | `entities[]`, `theme`, `tone`, `core_conflict` | `entities[]` → Stage 2 |
| Stage 2 | `physics_rules[]`, `social_rules[]` | `entities[]`, `rules[]` → Stage 3 |
| Stage 3 | `relationships{}`, `behavior_trees{}` | `relationships{}`, `behavior_trees{}` → Stage 4 |
| Stage 4 | `sandbox.py` | `sandbox.py` → Stage 5 |
| Stage 5 | `tuning_report.md` | 最终交付物 |

---

## 最小校验规则

| 阶段 | 必填字段 | 完成判定 |
|------|----------|----------|
| Stage 1 | `entities[]` 非空, `theme` 非空 | 实体数 ≥ 1 且主题已推断 |
| Stage 2 | `rules[]` 非空且均为现实规则 | 无超自然元素 |
| Stage 3 | `relationships{}` 非空, `behavior_trees{}` 非空 | 每个核心角色均有对应行为树 |
| Stage 4 | `sandbox.py` 可解析，无语法错误 | import mesa 成功 |
| Stage 5 | 沙盘可运行，进度输出正常 | tick > 0 |

---

## 下一步

进入 `02_workflow_builder`，由其负责：
1. 生成完整的 `human_agent_boundary.md`
2. 生成 `skills_manifest.md`（记录 Mesa 等依赖）
3. 生成 `activation_ready.md`
4. 生成 `tuning_report.md`
5. 生成 `run_experiment.md`
