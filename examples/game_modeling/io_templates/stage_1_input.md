# stage_1_input

purpose: 输入游戏规则并定义建模边界
required_fields:
- game_name
- rule_text
- player_set
optional_fields:
- hidden_information_rules
- time_horizon
example_content: 两人零和回合制游戏规则与胜负计分方式
done_criteria: 规则可被解析为玩家、行动、回合与终局条件
