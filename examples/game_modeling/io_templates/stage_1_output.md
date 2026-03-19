# stage_1_output

purpose: 输出形式化博弈定义
required_fields:
- players
- action_space
- payoff_definitions
- transition_rules
optional_fields:
- assumption_registry
- modeling_risks
example_content: 每位玩家可行动作、收益矩阵或收益函数、状态转移规则
done_criteria: payoff 与 transition 均可计算且字段齐全
