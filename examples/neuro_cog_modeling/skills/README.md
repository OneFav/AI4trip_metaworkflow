# Neuro-Cognitive Modeling Skills

This directory normally contains custom Python wrappers. However, thanks to our External Discovery process, we are utilizing **MCP Servers and Agent Skills** directly from the ecosystem for this workflow.

## Required External Skills

Before executing this workflow, ensure the following MCP servers / skills are installed or accessible:

1. **`literature-reviewer-skill` (from claw.club)**
   * **Stage:** Stage 1
   * **Purpose:** Systematic Chinese/English literature review across multiple academic databases.
   * **Local Snapshot:** `skills/academic-research/` has been downloaded from ClawHub via `clawhub inspect --file --json` for reproducible local execution when `clawhub install` hits rate limits.

2. **`Jupyter MCP Server` (e.g., `jjsantos01/jupyter-notebook-mcp`)**
   * **Stage:** Stage 4 & 5
   * **Purpose:** Provides an interactive sandbox to run Python code (PyMC, HDDM) locally, avoiding the need for hardcoded Python wrapper scripts.

3. **`plotly-data-visualization` (from MCP Market)**
   * **Stage:** Stage 5
   * **Purpose:** Generates publication-ready visualizations of the cognitive models and posterior distributions.

## How to use HDDM in this workflow

Instead of a local wrapper, the Agent should:
1. Connect to the Jupyter MCP Server.
2. Insert a cell to import `hddm` and load the dataset.
3. Execute the MCMC sampling interactively.
4. Read the text/image output directly from the Jupyter cell.
