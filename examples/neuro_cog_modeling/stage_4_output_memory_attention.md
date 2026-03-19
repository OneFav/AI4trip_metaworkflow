# Stage 4 Output: Memory-Attention Fitting Build

## generated_artifacts
- workflows/neuro_cog_modeling/stage_4_model_spec_memory_attention.json
- workflows/neuro_cog_modeling/model_fit_memory_attention.py
- workflows/neuro_cog_modeling/io_templates/stage_4_input.md
- workflows/neuro_cog_modeling/io_templates/stage_4_output.md

## verification
- pymc_builder generation: success
- generated script syntax check: success (`python -m py_compile`)
- runtime fitting execution: blocked by environment dependency conflict

## environment_issue
- Installing PyMC on current Python 3.12 introduced incompatible dependency branches:
  - PyMC latest requires `pytensor>=2.38` which requires `numpy>=2.0`
  - Existing local scientific stack in this environment expects `numpy<2` for parts of pandas/pyarrow ecosystem
- Result: no stable combination found in current global interpreter for immediate end-to-end fitting run.

## next_action_recommended
- Use isolated environment for Stage 4 fitting:
  - Python 3.11 virtual environment
  - `pip install pymc arviz pandas numpy`
  - Run `model_fit_memory_attention.py` with real dataset

## stage4_status
- status: partial_ready
- reason: code and templates are ready; fitting is blocked by interpreter dependency matrix.
