# Input Spec

## Required Input

* `code_path`: 代码仓库路径或主代码文件路径

## Optional Inputs

* `dataset_manifest.md`: 数据来源、切分、许可信息
* `env_lock.yml`: 环境锁定文件
* `existing_results/`: 现有实验输出目录
* `target_template.tex`: CDC 模板
* `related_work_seed.bib`: 初始参考文献

## Missing Input Handling

1. 缺失 `dataset_manifest.md` 时，工作流会生成待补清单并降级实验覆盖范围。
2. 缺失 `env_lock.yml` 时，标记复现风险并输出环境不确定性说明。
3. 缺失模板时，先产出 markdown 短文稿并保留后续 LaTeX 转换接口。

## Suggested Format

1. 输入目录建议包含 `src/`, `configs/`, `scripts/`, `results/`。
2. 关键实验脚本建议在 `scripts/README.md` 提供运行示例。
