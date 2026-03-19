description: "Fallback PyMC 建模工具。在没有交互式 Jupyter 环境时，生成基础的贝叶斯模型脚本。"

---

# pymc_builder

Generates a PyMC state-space fitting script for the Stage 3 defended model.

## Usage

```bash
python main.py --spec <path_to_model_spec.json> --output <path_to_save_pymc_script.py>
```

## Example spec fields

- model_name
- observed_acc_column
- observed_rt_column
- interference_column
- demand_column
- rehearsal_column
- fatigue_column
- draws
- tune
