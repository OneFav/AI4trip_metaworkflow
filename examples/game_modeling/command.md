# Command

## Command name

`/game_modeling`

## Standard usage

`/game_modeling game_rules.md --mode balanced`

## Example

`/game_modeling ./inputs/chess_variant_rules.md --mode balanced --solver nashpy`

## Optional args

* `--mode conservative|balanced|aggressive`
* `--solver nashpy|gambit|mixed`
* `--sim-engine mesa|custom`
* `--budget-hours <int>`

## Default behavior

* 执行 stage_1 后停在 `checkpoint_model_freeze`
* 批准后执行 stage_2、stage_3
* stage_3 后停在 `checkpoint_consistency_gate`
* 批准后执行 stage_4 并输出最终报告
