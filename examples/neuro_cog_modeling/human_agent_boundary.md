# Human-Agent Boundary Protocol

## Workflow: neuro_cog_modeling

This document defines the strict checkpoints and boundaries between Human and Agent for the `neuro_cog_modeling` workflow.

### General Rules

* The Agent MUST STRICTLY STOP at all defined Checkpoints.
* The Agent is FORBIDDEN to auto-proceed across these points without explicit human approval.
* The Agent must output the required report and explicitly ask the user for permission to continue.

### Checkpoints

#### Checkpoint 1: Literature Review Approval (`checkpoint_literature_review`)

* **Location:** End of Stage 1
* **Agent Responsibility:** Output a comprehensive summary of the literature review on the two cognitive neuroscience phenomena. Present the extracted parameters and theoretical contradictions.
* **Human Responsibility:** Review the findings. Add, correct, or refute the literature summary. Approve to proceed to modeling.

#### Checkpoint 2: Model Hypothesis Selection (`checkpoint_model_hypothesis`)

* **Location:** End of Stage 2
* **Agent Responsibility:** Propose 2-3 mathematical modeling candidates (e.g., DDM, RL, Bayesian frameworks) that can unify the two phenomena. Detail the biological/psychological plausibility of each.
* **Human Responsibility:** Select the best framework or request adjustments. Approve the chosen model framework for the next stage.

#### Checkpoint 3: The Challenge-Response Loop (`checkpoint_challenge_response`)

* **Location:** Stage 3
* **Agent Responsibility:** Present the formal mathematical definitions of the chosen model. Wait for human challenges.
* **Human Responsibility:** MUST propose counter-example scenarios or edge cases to challenge the model's validity.
* **Agent Responsibility (Loop):** Adjust model structure or parameters to defend against the challenge.
* **Exit Condition:** Human explicitly states "Challenge passed" or "Approve model for fitting".

#### Checkpoint 4: Fitting Results & Visualization (`checkpoint_model_fitting`)

* **Location:** End of Stage 4
* **Agent Responsibility:** Present the results of the data fitting (e.g., AIC/BIC scores, posterior distributions) using the Jupyter MCP Server.
* **Human Responsibility:** Review the goodness-of-fit and statistical validity. Approve to proceed to the final report.

#### Checkpoint 5: Final Report Review (`checkpoint_final_report`)

* **Location:** End of Stage 5
* **Agent Responsibility:** Generate the final unified modeling report with Plotly visualizations.
* **Human Responsibility:** Final review and sign-off.
