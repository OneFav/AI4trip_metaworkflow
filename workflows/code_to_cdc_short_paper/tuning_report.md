# Tuning Report

## tuning_target_skills

* code_claim_extractor
* cdc_short_paper_writer

## tuning_method

1. 为 code_claim_extractor 增加“主张-证据-文件定位”输出约束。
2. 为 cdc_short_paper_writer 增加“CDC短文长度与结构优先级”约束。

## before_behavior

1. 倾向生成泛化描述，证据定位粒度不稳定。
2. 写作输出偏长，章节压缩不充分。

## after_behavior

1. 可稳定输出 claim matrix，且引用到具体文件或结果项。
2. 输出优先保留摘要、方法、结果、结论最小闭环。

## evaluation_result

部分达标。证据绑定完整性提升明显，篇幅控制可用但仍需人审裁剪。

## rollback_plan

若输出遗漏关键实验项，回退到 v0.1-stub 的默认模板并增加人工补充步骤。
