# 环境隔离与运行指南 (Environment & Execution Guide)

由于本项目依赖的 **PyMC (v5.x)** 及其张量引擎 **PyTensor** 对 Python 环境及 `numpy` 版本有严格要求（推荐 `numpy >= 2.0`），为避免与本地原有环境冲突，建议使用以下隔离环境进行拟合。

## 1. 推荐配置 (System Requirements)
- **Python**: 3.10 或 3.11 (推荐 3.11)
- **Conda** (推荐) 或 **Venv**
- **操作系统**: Windows 10/11 (已测试)

## 2. 隔离环境安装 (Setup Instructions)

### 方法 A: 使用 Conda (推荐)
Conda 可以自动处理编译 C++ 代码所需的依赖项。
```powershell
# 1. 创建环境
conda create -n neuro_cog python=3.11 -y

# 2. 激活环境
conda activate neuro_cog

# 3. 安装核心依赖
conda install -c conda-forge pymc arviz numpy>=2.0 pandas -y
```

### 方法 B: 使用 Venv
如果您习惯使用标准 Python venv：
```powershell
# 1. 创建并激活
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. 升级 pip 并安装依赖
pip install --upgrade pip
pip install "pymc>=5.10.0" "arviz>=0.16.0" "numpy>=2.0.0" pandas
```

## 3. 运行模型 (Running the Model)
在激活环境后，您可以直接运行：
```powershell
python model_fit_memory_attention.py
```

或者使用本项目提供的 **一键运行脚本**:
```powershell
.\run_modeling.ps1
```

## 4. 预期输出 (Expected Output)
1. **采样日志**: 显示 4 条链的采样进度（Progress bars）。
2. **可视化图表**:
   - `trace_plot.png`: 参数收敛图（Trace plots）。
   - `posterior_predictive.png`: 后验预测检查（PPC）。
3. **统计结果**: `summary_stats.csv` 包含参数的均值、标准差及 R-hat 收敛指标。
