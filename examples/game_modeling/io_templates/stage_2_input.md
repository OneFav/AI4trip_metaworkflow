# stage_2_input

purpose: 输入仿真执行所需结构化模型
required_fields:
- players
- action_space
- payoff_definitions
- transition_rules
optional_fields:
- simulation_budget
- seed_list
example_content: 仿真轮次、参数网格、随机种子清单
done_criteria: 可直接驱动批量仿真运行
