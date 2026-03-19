# Windows PowerShell 一键拟合脚本 (One-Click Fitting Script)

# 1. 检查 Python 环境
Write-Host "Checking Python environment..." -ForegroundColor Cyan

# 2. 检查必要的包
$requiredPackages = @("pymc", "arviz", "numpy", "pandas")
$missingPackages = @()

foreach ($pkg in $requiredPackages) {
    python -c "import $pkg" 2>$null
    if ($LASTEXITCODE -ne 0) {
        $missingPackages += $pkg
    }
}

if ($missingPackages.Count -gt 0) {
    Write-Host "Error: The following packages are missing or incompatible: $($missingPackages -join ', ')" -ForegroundColor Red
    Write-Host "Please refer to 'environment.md' for setup instructions." -ForegroundColor Yellow
    exit 1
}

# 3. 运行模型
Write-Host "Starting Bayesian State-Space Modeling (Memory & Attention)..." -ForegroundColor Green
Write-Host "This process may take 1-5 minutes depending on your CPU." -ForegroundColor Gray

python model_fit_memory_attention.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nSuccess! Results have been saved to the current directory." -ForegroundColor Green
    Write-Host "Check 'trace_plot.png' and 'summary_stats.csv' for details." -ForegroundColor Gray
} else {
    Write-Host "`nError: Model fitting failed. Check logs for details." -ForegroundColor Red
}
