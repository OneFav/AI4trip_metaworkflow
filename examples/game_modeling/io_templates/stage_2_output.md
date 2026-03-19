# stage_2_output

purpose: 输出仿真结果摘要与候选均衡点
required_fields:
- simulation_summary
- parameter_grid
- equilibrium_candidates
optional_fields:
- failed_runs
- logs_index
example_content: 平均收益、方差、策略收敛曲线与候选均衡
done_criteria: 至少包含一组可复现参数与对应统计结果
