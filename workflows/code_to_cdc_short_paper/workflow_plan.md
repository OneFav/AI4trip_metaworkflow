# Workflow Plan

## Meta

* based_on_intent: workflows/code_to_cdc_short_paper/intent.md
* created_at: 2026-03-18
* status: ready_for_build

## Suggested Workflow Type

code-to-paper with rigor enhancement

## Stage Design

### Stage 1

* id: stage_1
* name: 代码解析与主张抽取
* executor: Agent
* goal: 从代码、配置、日志中抽取方法假设、实现细节、已有结果与可证实主张
* outputs:
  * `artifacts/stage1_claim_matrix.md`
  * `artifacts/stage1_method_outline.md`

### Stage 2

* id: stage_2
* name: 严谨性缺口诊断与补强实验计划
* executor: Human-Agent
* goal: 定位论文严谨性缺口并形成可执行补强计划
* outputs:
  * `artifacts/stage2_rigor_gap_report.md`
  * `artifacts/stage2_experiment_plan.md`

### Checkpoint A

* id: checkpoint_a
* type: report-decision
* after_stage: stage_2
* agent_report:
  * 主张-证据矩阵
  * 缺口清单与优先级
  * 实验预算与预计时长
* human_decision:
  * 批准执行的实验子集
  * 拒绝或降级的实验项
  * 论文主结论的保留范围

### Stage 3

* id: stage_3
* name: 补强实验执行与统计分析
* executor: Agent
* goal: 执行批准实验并生成可复用结果资产
* outputs:
  * `artifacts/stage3_results_table.csv`
  * `artifacts/stage3_stats_report.md`
  * `figures/`

### Stage 4

* id: stage_4
* name: CDC短文草拟与证据对齐
* executor: Agent
* goal: 生成符合 CDC 短文结构的论文初稿并完成图表引用绑定
* outputs:
  * `paper/draft_v1.md`
  * `paper/fig_table_mapping.md`

### Stage 5

* id: stage_5
* name: 人审修订与投稿包收口
* executor: Human-Agent
* goal: 完成高风险表述修订、格式检查、引用与复现说明收口
* outputs:
  * `paper/final_short_paper.md`
  * `paper/submission_checklist.md`
  * `artifacts/reproducibility_note.md`

## Capability Mapping

1. 代码理解与主张抽取
2. 实验编排与批运行
3. 统计检验与误差分析
4. 学术写作与结构化压缩
5. 图表资产管理与交叉引用
6. 投稿合规检查

## Candidate Skills

* local_candidate:
  * code_claim_extractor
  * experiment_rigor_runner
  * cdc_short_paper_writer
  * submission_compliance_checker
* external_candidate:
  * latex_template_adapter
  * bib_quality_checker

## Human-Agent Boundary

* Human:
  * 决定最终研究主张边界
  * 决定是否保留负向结果
  * 决定投稿版本取舍
* Agent:
  * 自动执行可重复实验
  * 自动生成统计与图表
  * 自动生成论文草稿与格式检查报告
* Human-Agent:
  * checkpoint 决策
  * 关键结论措辞收敛

## Next Step

进入 `workflow_builder`，落盘 workflow 包与技能清单，并执行一次实验化 dry-run 校验。
