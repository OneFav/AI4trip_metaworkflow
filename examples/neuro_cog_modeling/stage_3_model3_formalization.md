# Stage 3 Working Draft: Model-3 Formalization (Memory Trace × Attention)

## Chosen Model
Bayesian State-Space Coupling Model

## Latent Dynamics
For participant i at trial t:

M_{i,t} ~ Normal(mu_M_{i,t}, sigma_M)
mu_M_{i,t} = alpha_M * M_{i,t-1} + beta_M * A_{i,t-1} - gamma_M * I_{i,t} + kappa_M * A_{i,t-1} * U_{i,t}

A_{i,t} ~ Normal(mu_A_{i,t}, sigma_A)
mu_A_{i,t} = alpha_A * A_{i,t-1} + delta_A * D_{i,t} - eta_A * I_{i,t} - phi_A * F_{i,t}

Where:
- M: memory trace strength
- A: allocated attention
- I: external interference intensity
- D: task demand signal
- U: rehearsal/refresh input
- F: fatigue term

## Observation Model
Accuracy:

y_{i,t}^{acc} ~ Bernoulli(sigmoid(w0 + w1 * M_{i,t} + w2 * A_{i,t} + w3 * M_{i,t} * A_{i,t}))

Reaction time:

y_{i,t}^{rt} ~ LogNormal(mu_{rt,i,t}, sigma_rt)
mu_{rt,i,t} = r0 - c1 * M_{i,t} - c2 * A_{i,t} + c3 * I_{i,t}

## Priors (initial proposal)
- alpha_M, alpha_A ~ Beta(8, 2)
- beta_M, delta_A, kappa_M ~ HalfNormal(1.0)
- gamma_M, eta_A, phi_A ~ HalfNormal(1.0)
- w0 ~ Normal(0, 1.5)
- w1, w2, w3 ~ Normal(0, 1.0)
- r0 ~ Normal(0, 1.0)
- c1, c2, c3 ~ HalfNormal(1.0)
- sigma_M, sigma_A, sigma_rt ~ HalfNormal(1.0)

## Identifiability Constraints
- M_{i,0}, A_{i,0} standardized to N(0,1)
- Inputs I, D, U, F z-scored per participant
- If severe collinearity between D and U: freeze one pathway in first fit

## Predicted Phenomena
1. High interference reduces attention first, then degrades memory trace.
2. Rehearsal rescues memory only when attention is not fully depleted (gated by A).
3. Short-term high load may show temporary RT increase before accuracy collapse.

## Challenge Interface (for Human)
Please provide at least 3 counter-examples.
Recommended structure:
- Scenario A (expected to break the model): ...
- Scenario B (boundary case): ...
- Scenario C (paradoxical observation): ...

## Expected Stage-3 Output
- For each challenge: failure diagnosis + model patch
- Updated equations and parameter constraints
- Decision whether model is approved for Stage 4 fitting
