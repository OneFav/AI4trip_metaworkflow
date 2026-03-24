# Input Spec

## 必需输入

- 一个输入文件（建议为 YAML 或 Markdown），包含：
  - grn_items：一个或多个 GRN/模块的标识与数据路径
  - grn_observation_level：观测层级（module/regulon/pathway/perturbation）
  - prototype_library_ref：任务原型库版本或路径

## 可选输入

- ann_candidates：候选 ANN 家族或模型路径
- probe_family_overrides：probe family 的覆盖参数
- validation_policy：验证策略（相关性、排序一致性、负对照）
- distance_metric：GW / Frobenius / rank correlation

## 缺少输入的处理

- 未提供 ann_candidates 时使用默认 ANN 家族列表
- 未提供 probe_family_overrides 时使用原型库默认设置
- 未提供 validation_policy 时启用最小验证集合

## 建议格式示例（YAML）

grn_items:
  - id: grn_01
    source: data/grn/grn_01.json
  - id: grn_02
    source: data/grn/grn_02.json
grn_observation_level: module
prototype_library_ref: data/prototypes/v1
ann_candidates:
  - sparse_mlp
  - gru
  - ssm
validation_policy:
  correlation: true
  rank_consistency: true
  ablation: true
