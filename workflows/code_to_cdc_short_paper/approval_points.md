# Approval Points

## Checkpoint A

* checkpoint_name: rigor_plan_approval
* trigger: 完成 `stage_2` 严谨性缺口报告后触发
* agent_report_required:
  * 主张-证据矩阵
  * 缺口优先级
  * 实验资源预算
  * 预期风险
* human_decision_required:
  * 批准或拒绝实验子项
  * 决定是否引入额外基线
  * 决定投稿周期是否允许补做实验
* if_rejected:
  * 回退到 `stage_2` 重排计划
  * 更新主张边界并缩减稿件目标

## Checkpoint B

* checkpoint_name: draft_submission_gate
* trigger: 完成 `stage_4` 论文草稿后触发
* agent_report_required:
  * 章节完整性检查
  * 图表-结论绑定检查
  * 格式合规预检查
* human_decision_required:
  * 决定是否进入最终稿
  * 决定删减或增强的段落
* if_rejected:
  * 回退 `stage_4` 或 `stage_3`
  * 记录拒绝原因至 `paper/revision_log.md`
