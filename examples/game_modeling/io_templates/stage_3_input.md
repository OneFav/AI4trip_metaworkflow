# stage_3_input

purpose: 输入数学求解阶段的数据与边界
required_fields:
- simulation_summary
- parameter_grid
- observed_equilibrium_candidates
optional_fields:
- symbolic_assumptions
- numerical_tolerance
example_content: 从仿真提取的候选点、参数区间与求解精度
done_criteria: 可直接进入解析或数值求解
