# Skill Registry

> This file stores normalized entries that AI4Trip can reason over quickly.
> Entries here do NOT necessarily mean the skills are installed locally.
> They mean AI4Trip already knows these sources and can consider them during workflow solving.

---

## Entry Format
- id
- name
- type
- source
- url
- tags
- suitable_for
- local_status
- notes

---

## Entries

### entry_001
- id: aris_research_workflow
- name: ARIS
- type: external_workflow_source
- source: guidebook
- url: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
- tags: [research, review-loop, experiment, markdown-skills, automation]
- suitable_for:
  - research_from_zero
  - experiment_iteration
  - review_loop_reference
- local_status: not_installed
- notes: strong source for autonomous research execution patterns; keep separate from AI4Trip's own scene-based positioning

### entry_002
- id: orchestra_research_skills
- name: AI Research Engineering Skills
- type: external_skill_library
- source: guidebook
- url: https://github.com/zechenzhangAGI/claude-ai-research-skills
- tags: [research, engineering, training, eval, rag, multimodal, mlops]
- suitable_for:
  - experiment_design
  - model_training
  - evaluation_workflows
- local_status: not_installed
- notes: broad and high-value source for concrete research engineering skills

### entry_003
- id: levnikolaevich_claude_code_skills
- name: Claude Code Skills Collection
- type: external_skill_library
- source: guidebook
- url: https://github.com/levnikolaevich/claude-code-skills
- tags: [development, planning, qa, agile, workflow]
- suitable_for:
  - coding_workflows
  - project_planning
  - review_and_quality_gates
- local_status: not_installed
- notes: useful for non-research workflow pieces such as planning and execution discipline

### entry_004
- id: awesomeskills_directory
- name: Awesome Skills
- type: external_directory
- source: guidebook
- url: https://www.awesomeskills.dev/
- tags: [directory, discovery, skills, codex, claude, cursor]
- suitable_for:
  - skill_discovery
  - source_expansion
- local_status: not_applicable
- notes: use as a discovery portal before broader open web search

### entry_005
- id: autora_framework
- name: AutoRA
- type: external_framework
- source: guidebook
- url: https://github.com/AutoResearch/autora
- tags: [science, empirical-research, experiment-design, data-collection]
- suitable_for:
  - empirical_workflow_patterns
  - discovery_cycles
- local_status: not_installed
- notes: useful as a workflow-pattern source rather than a plug-and-play skill pack

### entry_006
- id: claude_skillkit
- name: Claude Skill Kit
- type: external_skill_builder
- source: guidebook
- url: https://github.com/rfxlamia/claude-skillkit
- tags: [skill-building, validation, packaging, qa]
- suitable_for:
  - wrapping_external_skills
  - validating_imported_skills
- local_status: not_installed
- notes: useful for AI4Trip when it later wraps or standardizes outside skills