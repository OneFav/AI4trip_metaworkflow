# code_to_cdc_short_paper

从已验证有效性的代码项目快速生成 CDC 短文论文草稿，并补齐严谨性证据链。

## 适用场景

* 已有代码与初步实验
* 缺乏论文级严谨性证据
* 需要在较短周期产出短文投稿稿

## 调用方式

`/code_to_cdc_short_paper <code_path> --paper-type cdc_short`

## 人机分工

* Human：主张边界与风险句定稿
* Agent：代码解析、补强实验、文稿初稿
* Human-Agent：checkpoint 决策与最终收口

## 当前局限

1. 默认输出 markdown 稿，LaTeX 精细排版依赖外部模板适配。
2. 外部文献质量检查能力尚未本地安装。
