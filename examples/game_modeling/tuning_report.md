# Tuning Report

## tuning_target_skills

* game_rule_formalizer
* consistency_checker

## tuning_method

* 对 game_rule_formalizer 增加“变量命名一致性 + 收益函数可计算表达”约束
* 对 consistency_checker 增加“一致/不一致条目分层输出”约束

## before_behavior

* 形式化输出可读性不稳定，变量别名冲突较多
* 一致性报告偏叙述化，难以做回归比较

## after_behavior

* 模型定义中的玩家、行动、收益字段可稳定对齐模板
* 一致性报告可输出结构化差异项与疑点等级

## evaluation_result

partial_pass

## rollback_plan

若结构化字段缺失，回退到 v0.1-stub 模板并要求人工补齐字段后重跑。
