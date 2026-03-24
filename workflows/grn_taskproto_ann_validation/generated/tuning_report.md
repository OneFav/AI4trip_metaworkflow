# Tuning Report

tuning_target_skills:
  - distance_engine
  - result_reporter

tuning_method:
  - prompt_refinement

before_behavior:
  - distance_engine 输出仅包含距离数值，缺少 metric 与稳定性摘要
  - result_reporter 缺少对置信区间与负对照的显式引用

after_behavior:
  - distance_engine 输出包含 metric、bootstrap 稳定性摘要
  - result_reporter 强制包含置信度与失败案例段落

evaluation_result:
  - 满足当前 workflow 的最小可用阈值

rollback_plan:
  - 若输出字段不稳定，回退到简化的距离排序输出
