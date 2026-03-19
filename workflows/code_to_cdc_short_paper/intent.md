# Workflow Intent

## Meta

* workflow_name: code_to_cdc_short_paper
* created_at: 2026-03-18
* source: user_request

## Goal

从一个已验证方法有效性的代码文件出发，产出一篇可投稿 CDC 的短文论文初稿，并补齐论文严谨性所需的证据链。

## Scene

桌面科研写作与实验复现。

## Design Intent

1. 直接以代码仓库为输入，不依赖先验论文草稿。
2. 先抽取方法主张与证据，再补做严谨性增强实验与分析。
3. 在进入全文写作前设置强制 checkpoint，避免“证据不足就成文”。
4. 输出同时覆盖投稿文本、复现实验记录、图表资产和合规检查结果。

## Inputs

* 必需：`code_path`
* 推荐：`dataset_manifest.md`、`env_lock.yml`、`existing_results/`
* 可选：`target_template.tex`、`related_work_seed.bib`

## Success Criteria

1. 有完整 CDC 短文结构稿。
2. 关键结论均可回链到代码或实验产物。
3. 至少包含一轮严谨性补强结果：统计显著性、消融、鲁棒性或误差分析中的若干项。
4. 输出可复现实验说明与产物索引。

## Human-Agent Boundary Preference

* Human 主导：研究问题边界、贡献声明最终定稿、伦理与表述风险判断。
* Agent 主导：代码解读、实验编排执行、图表初稿、文本初稿与格式化。
* Human-Agent 协作：checkpoint 审核、结论收敛、投稿前删减与重写。
