# Stage 4 Output: 模型拟合结果

## purpose
记录模型编码、采样与拟合评估结果，供 Stage 5 解释与报告使用。

## required_fields
- generated_script_path
- run_status
- posterior_summary
- fit_metrics
- diagnostics

## optional_fields
- trace_plot_path
- ppc_plot_path
- model_comparison

## example_content
- generated_script_path: workflows/neuro_cog_modeling/model_fit_memory_attention.py
- run_status: success
- posterior_summary:
  - alpha_M: mean=0.81, hdi_3%=0.74, hdi_97%=0.88
  - kappa_M: mean=0.42, hdi_3%=0.28, hdi_97%=0.57
  - w3: mean=0.31, hdi_3%=0.09, hdi_97%=0.52
- fit_metrics:
  - waic: 1832.4
  - loo: 1840.1
- diagnostics:
  - rhat_max: 1.01
  - ess_min: 720

## done_criteria
- 关键参数后验可解释
- 收敛诊断达标（如 R-hat 接近 1）
- 输出可供 Stage 5 直接引用
