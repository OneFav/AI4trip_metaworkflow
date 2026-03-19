# Command

## Command Name

`/code_to_cdc_short_paper`

## Standard Usage

`/code_to_cdc_short_paper <code_path> --paper-type cdc_short --mode balanced`

## Example

`/code_to_cdc_short_paper ./projects/my_method --paper-type cdc_short --with-existing-results ./results`

## Optional Arguments

* `--paper-type cdc_short`：固定短文模式
* `--mode conservative|balanced|aggressive`：自动化强度
* `--budget-hours <int>`：实验预算上限
* `--template <path>`：LaTeX 模板路径

## Default Behavior

1. 先执行 stage_1 到 stage_2。
2. 在 Checkpoint A 停止等待人类决策。
3. 获批后执行 stage_3 到 stage_4。
4. 在 Checkpoint B 停止等待人类确认是否进入最终稿。
