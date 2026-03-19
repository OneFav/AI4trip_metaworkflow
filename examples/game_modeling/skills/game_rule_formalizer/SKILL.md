---
name: "game_rule_formalizer"
description: "将自然语言规则形式化为博弈模型。使用 OpenSpiel 或自定义映射逻辑将规则转为状态/策略/收益结构。当用户提供新游戏规则并需要建模时调用。"
---

# Game Rule Formalizer

## Implementation Logic

1.  **Rule Parsing**: 接收自然语言博弈规则描述。
2.  **Structural Mapping**:
    *   识别 `players` 集合。
    *   定义 `action_space` (discrete/continuous)。
    *   推导 `payoff_functions` 或 `payoff_matrix`。
    *   识别 `transition_rules` (deterministic/stochastic)。
3.  **Integration**:
    *   生成符合 `OpenSpiel` 的 `Python` 环境类或符合 `Nashpy` 的博弈矩阵。
    *   输出 `stage_1_output.json` 供后续阶段使用。

## Dependencies
- `OpenSpiel` (可选, 用于复杂博弈)
- `LLM` (用于初步规则提取)

## Usage
```bash
python main.py stage_1_input.json
```
