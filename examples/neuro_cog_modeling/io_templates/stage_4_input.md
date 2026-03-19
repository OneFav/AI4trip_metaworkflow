# Stage 4 Input: 模型编码与数据拟合

## purpose
将 Stage 3 修补后的模型3转为可运行代码并进行参数拟合。

## required_fields
- data_file_path: 行为数据 CSV 路径
- observed_acc_column: 准确率列名（0/1）
- observed_rt_column: 反应时列名（正数）
- interference_column: 干扰强度列名
- demand_column: 任务需求列名
- rehearsal_column: 复述/刷新列名
- fatigue_column: 疲劳列名

## optional_fields
- draws: MCMC 抽样数
- tune: 预热步数
- model_variant: soft_gating 或 hard_gating

## example_content
- data_file_path: data/memory_attention_trials.csv
- observed_acc_column: acc
- observed_rt_column: rt
- interference_column: I
- demand_column: D
- rehearsal_column: U
- fatigue_column: F
- draws: 1000
- tune: 1000
- model_variant: soft_gating

## done_criteria
- 成功生成可运行的 PyMC 拟合脚本
- 拟合运行完成并得到后验样本
- 输出关键参数摘要与拟合指标
