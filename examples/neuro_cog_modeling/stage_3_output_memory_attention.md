# Stage 3 Output: Defended Model (Scenario C)

## Challenge Adopted
- Scenario C: 复述/刷新 \(U\) 只有在高注意状态下才有效；低注意时 \(U\) 基本无效。

## Why Original Model Fails
- 原模型把复述项写成 \(+ \kappa_M U_{i,t}\)，等价于“只要复述就总能增益记忆痕迹”。
- 该假设忽略了注意资源门控，无法解释“低注意时复述失效”。

## Model Patch

### 1) Replace direct rehearsal term with gated rehearsal term
- Before:
  - \(\mu_{M,i,t} = \alpha_M M_{i,t-1} + \beta_M A_{i,t-1} - \gamma_M I_{i,t} + \kappa_M U_{i,t}\)
- After:
  - \(\mu_{M,i,t} = \alpha_M M_{i,t-1} + \beta_M A_{i,t-1} - \gamma_M I_{i,t} + \kappa_M A_{i,t-1} U_{i,t}\)

### 2) Optional hard-threshold gating (ablation)
- \(g_{i,t-1} = \mathbb{I}(A_{i,t-1} > \tau_A)\)
- \(\mu_{M,i,t} = \alpha_M M_{i,t-1} + \beta_M A_{i,t-1} - \gamma_M I_{i,t} + \kappa_M g_{i,t-1} U_{i,t}\)

## Updated Priors / Constraints
- \(\kappa_M \sim \text{HalfNormal}(1.0)\)
- \(A\) 已标准化到 \([z]\) 空间，避免乘积项数值爆炸
- 若采用阈值门控：\(\tau_A \sim \text{Normal}(0, 0.5)\)

## New Testable Predictions
- 在低 \(A\) 条件下，提高 \(U\) 对准确率提升应接近 0。
- 在高 \(A\) 条件下，提高 \(U\) 对准确率提升显著且 RT 改善。
- \(U\) 的主效应将变弱，\(A \times U\) 交互项显著增强。

## Stage 3 Decision
- 针对 Scenario C 的质疑，模型已完成结构修补。
- 当前模型可进入 Stage 4 进行拟合验证（建议同时比较 soft-gating 与 hard-gating 两个版本）。
