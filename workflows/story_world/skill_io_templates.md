# Skill I/O Templates: story_world

本文档定义 `story_world` 工作流各阶段之间的输入/输出文件模板，确保每个阶段输入来源清晰、输出去向明确、字段可校验。

---

## Stage 1: 实体与意图抽取

### 输入模板: `io_templates/stage1_input_story.md`

```markdown
# 故事输入

## 故事文本
<!-- 用户在此粘贴完整的故事文本 -->

## 额外约束（可选）
<!-- 用户可在此补充额外的世界设定或约束 -->
```

### 输出模板: `io_templates/stage1_output_entities.md`

```markdown
# Stage 1 输出：实体与意图清单

## 抽取的实体

### 角色 (characters)
- name: <角色名>
  description: <角色描述>
  importance: high/medium/low  # 核心/重要/次要

### 地点 (locations)
- name: <地名>
  description: <地点描述>
  importance: high/medium/low

### 道具/物品 (objects)
- name: <物品名>
  description: <物品描述>
  importance: high/medium/low

## 核心意图推断

### 主题 (theme)
<Agent 推断的主题，如：阶级冲突、人性善恶、孤独与连接>

### 基调 (tone)
<Agent 推断的基调，如：压抑、温暖、讽刺、悬疑>

### 主要矛盾 (core_conflict)
<Agent 推断的核心戏剧冲突>
```

---

## Stage 2: 世界规则推断

### 输入模板: `io_templates/stage2_input_entities.md`

```markdown
# Stage 2 输入：实体清单

<!-- 继承 Stage 1 的完整输出 -->
```

### 输出模板: `io_templates/stage2_output_rules.md`

```markdown
# Stage 2 输出：世界规则建议

## 物理规则 (physics_rules)
- rule: <规则描述>
  source: <推断来源（故事文本依据）>
  is_supernatural: false  # 必须为 false

## 社会规则 (social_rules)
- rule: <社会规范/规则描述>
  source: <推断来源>
  is_supernatural: false
  affected_characters: [<受影响角色列表>]

## 规则校验状态
- all_realistic: true/false
- violations: []  # 如果有超自然元素，列出此处
```

---

## Stage 3: 关系与行为建模

### 输入模板: `io_templates/stage3_input_rules.md`

```markdown
# Stage 3 输入：世界规则

<!-- 继承 Stage 2 的完整输出 -->
```

### 输出模板: `io_templates/stage3_output_model.md`

```markdown
# Stage 3 输出：关系与行为模型

## 角色关系网络 (relationships)

### 关系图谱
- source: <角色A>
  target: <角色B>
  type: ally/enemy/neutral/family/未知
  description: <关系描述>
  strength: 0.0-1.0  # 关系强度

## Agent 行为决策树 (behavior_trees)

### <角色名>
- type: behavior_tree
- root_state: <根状态>
- transitions:
    - from: <状态A>
      to: <状态B>
      condition: <触发条件>
      action: <执行动作>
- initial_resources:  # 初始资源/属性
    - <属性名>: <初始值>
```

---

## Stage 4: 沙盘代码生成

### 输入模板: `io_templates/stage4_input_model.md`

```markdown
# Stage 4 输入：关系与行为模型

<!-- 继承 Stage 3 的完整输出 -->
```

### 输出文件

* **输出路径**: `worlds/<world_name>/sandbox.py`
* **输出格式**: 完整的 Mesa 框架 Python 代码
* **必须包含**:
    * `Agent` 类（每个角色一个类或共享类）
    * `Model` 类（含 `schedule`、空间初始化）
    * `space`: GridSpace 或 ContinuousSpace
    * `visualization`: 包含可视化服务器配置
    * `main`: 包含模型初始化与运行循环

---

## Stage 5: 沙盘验证与调优

### 输入文件

* **输入路径**: `worlds/<world_name>/sandbox.py`

### 输出模板: `tuning_report.md`

```markdown
# 沙盘调优报告

## 运行结果

### 执行的 tick 数
<number>

### 关键指标
- <指标名>: <值>

## 发现的问题

### 问题 1
- description: <问题描述>
- suggested_fix: <建议修复方案>

## 调优建议

### 建议 1
- parameter: <参数名>
  current_value: <当前值>
  suggested_value: <建议值>
  reason: <原因>
```

---

## 字段映射总览

| 阶段 | 关键输出字段 | 传递给下一阶段的字段 |
|------|-------------|---------------------|
| Stage 1 | `characters[]`, `locations[]`, `objects[]`, `theme`, `tone`, `core_conflict` | `characters[]` + `locations[]` + `objects[]` → Stage 2 |
| Stage 2 | `physics_rules[]`, `social_rules[]`, `all_realistic` | `rules[]` → Stage 3 |
| Stage 3 | `relationships[]`, `behavior_trees{}` | `relationships[]` + `behavior_trees{}` → Stage 4 |
| Stage 4 | `sandbox.py` | `sandbox.py` → Stage 5 |
| Stage 5 | `tuning_report.md` | 最终交付物 |

---

## 最小校验规则

| 阶段 | 必填字段 | 格式要求 |
|------|----------|----------|
| Stage 1 | `characters[]`, `theme`, `tone` | 非空数组/字符串 |
| Stage 2 | `rules[]`, `all_realistic: true` | `is_supernatural` 必须全为 `false` |
| Stage 3 | `relationships[]`, `behavior_trees{}` | 每个 `high importance` 角色必须有对应 `behavior_tree` |
| Stage 4 | `sandbox.py` | Python 文件，可 `import mesa` |
| Stage 5 | `tick > 0` | 沙盘可运行 |
