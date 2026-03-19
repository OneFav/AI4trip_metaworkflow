# Approval Points

## checkpoint_model_freeze

* trigger: stage_1 完成后触发
* agent_report_required:
  * 玩家集合与策略空间定义
  * 收益函数与状态转移规则
  * 假设清单与简化影响说明
* human_decision_required:
  * 批准进入 stage_2 / stage_3
  * 要求补充或修改建模定义
* reject_action:
  * 回退到 stage_1
  * 更新 `artifacts/model_assumptions.md` 后重提审批

## checkpoint_consistency_gate

* trigger: stage_3 完成后触发
* agent_report_required:
  * 仿真统计摘要
  * 数学求解结果
  * 一致性与偏差项说明
* human_decision_required:
  * 批准进入 stage_4 输出结论
  * 要求追加实验或更换求解方法
* reject_action:
  * 回退到 stage_2 或 stage_3
  * 记录偏差原因至 `artifacts/consistency_issues.md`
