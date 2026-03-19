# Skill Sources Guide

> This file is a guidebook, not a local skill inventory.
> Entries here are candidate sources of skills / workflows / frameworks that AI4Trip may consult, reference, or later wrap.
> Being listed here does NOT mean the skill is already downloaded, installed, or directly callable.

---

## 1. How to use this guide

AI4Trip should use this file in two stages:

### Fast path
- Quickly check whether an existing source here already covers the user's need.
- Prefer reuse of known, documented, active sources.

### Slow path
- If no source here is suitable, escalate to broader web search.
- New useful sources may later be added back into this guide.

---

## 2. Source Entry Format

Each source should be described with:
- Name
- Type
- Focus
- Why it matters
- Good for
- Cautions
- URL

---

# 3. Curated Initial Sources

## D. Document & LaTeX Skills

### 7. latex-document-skill (ndpvt-web)
- Type: LaTeX document generation skill
- Focus: Universal LaTeX template, PDF generation, academic document automation
- Why it matters:
  - comprehensive LaTeX templates for papers, reports, resumes, theses
  - includes BibTeX auto-fetch, OCR to LaTeX, LaTeX diff tools
  - supports poster generation (NeurIPS, conference posters)
- Good for:
  - academic paper formatting
  - PDF report generation
  - Beamer presentations
  - multi-pass compilation workflows
- Cautions:
  - requires local TeX distribution (TeX Live, MiKTeX)
  - compilation scripts are bash-based (needs adaptation for Windows)
- URL:
  - https://github.com/ndpvt-web/latex-document-skill

### 8. claude-scientific-writer (K-Dense-AI)
- Type: scientific writing skill library
- Focus: academic paper generation with LaTeX/PDF output
- Why it matters:
  - generates publication-ready LaTeX tables
  - creates CONSORT flowcharts for clinical trials
  - supports Kaplan-Meier curves and statistical visualizations
- Good for:
  - scientific figure generation
  - LaTeX table creation
  - academic document formatting
- Cautions:
  - specialized for scientific/medical documents
  - requires statistical packages (R, Python with scipy)
- URL:
  - https://github.com/K-Dense-AI/claude-scientific-writer

---

## A. Research automation / research workflow

### 1. ARIS — Auto-Research-In-Sleep
- Type: research workflow / markdown skill system
- Focus: autonomous ML research workflow, idea discovery, review loop, experiment automation
- Why it matters:
  - very strong reference for "research execution + critique loop"
  - lightweight markdown-only design
  - supports Claude Code / Codex / OpenClaw / Cursor style usage
- Good for:
  - review loop
  - research pipeline examples
  - idea-to-experiment orchestration
- Cautions:
  - its core narrative is "sleep-time research automation", which should not overwrite AI4Trip's own positioning
  - some capabilities are pipeline-heavy rather than meta-workflow-oriented
- URL:
  - https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep

### 2. AutoRA
- Type: empirical research automation framework
- Focus: model discovery, experimental design, data collection, documentation
- Why it matters:
  - useful as a workflow-pattern reference
  - helpful when AI4Trip needs to reason about iterative empirical discovery
- Good for:
  - workflow patterns
  - experiment cycle design
  - scientific discovery structure
- Cautions:
  - not a Claude/OpenClaw skills pack
  - more framework-like than plug-and-play skill-like
- URL:
  - https://github.com/AutoResearch/autora

---

## B. Research engineering skill libraries

### 3. AI Research Engineering Skills (Orchestra Research)
- Type: research engineering skill library
- Focus: 70 research/engineering skills for AI agents
- Why it matters:
  - one of the strongest current sources for research-oriented skills
  - covers model architecture, tokenization, fine-tuning, RLHF, distributed training, inference, RAG, multimodal, prompt engineering, MLOps
- Good for:
  - importing or wrapping concrete research skills
  - AI4Trip workflows related to experiment design, training, eval, deployment
- Cautions:
  - large and broad; should be selectively used rather than imported wholesale
  - many entries are framework-specific
- URL:
  - https://github.com/zechenzhangAGI/claude-ai-research-skills

### 4. claude-code-skills (levnikolaevich)
- Type: Claude Code skills collection
- Focus: full Agile development workflow, planning, execution, QA, Linear integration
- Why it matters:
  - useful beyond research itself
  - strong reference for workflow packaging, phase structure, and engineering-oriented skills
- Good for:
  - planning
  - coding workflow
  - project and quality gates
- Cautions:
  - more software-delivery-oriented than research-specific
  - AI4Trip should only borrow relevant parts
- URL:
  - https://github.com/levnikolaevich/claude-code-skills

---

## C. Skill discovery / plugin ecosystem

### 5. Awesome Skills
- Type: skill directory / discovery portal
- Focus: living index of skills for Claude Code, Codex, Cursor, and other agent platforms
- Why it matters:
  - useful as a search hub before doing broader open web search
  - can help AI4Trip discover new skill collections quickly
- Good for:
  - directory lookup
  - external skill discovery
  - keeping up with new skill packs
- Cautions:
  - not all indexed skills are equally mature
  - directory listing is not the same as quality validation
- URL:
  - https://www.awesomeskills.dev/

### 6. cblecker / Claude Plugins
- Type: plugin marketplace / Claude Code skill entry point
- Focus: plugin install flow and marketplace-based skill usage
- Why it matters:
  - useful reference for how skill discovery and installation can be abstracted
- Good for:
  - thinking about AI4Trip's future "skill onboarding" layer
  - plugin style packaging
- Cautions:
  - marketplace-centered, not research-centered
- URL:
  - https://github.com/cblecker/claude-plugins

---

## D. Skill-building and wrapping

### 7. Claude Skill Kit
- Type: skill creation toolkit
- Focus: building, validating, and packaging Claude Code skills
- Why it matters:
  - useful when AI4Trip wants to wrap external skills into its own protocol
  - strong reference for skill QA and validation logic
- Good for:
  - wrapping
  - validating imported skills
  - improving skill quality
- Cautions:
  - it helps create skills, not directly solve user tasks
- URL:
  - https://github.com/rfxlamia/claude-skillkit

---

# 4. How AI4Trip should reason over these sources

When a user asks for a workflow, AI4Trip should not immediately search the whole web.

Recommended order:

1. Check local workflow patterns
2. Check this guidebook for likely sources
3. Check already-known registry entries
4. If still unresolved, escalate to broader external search
5. Only after human confirmation should any external source be downloaded or wrapped

---

# 5. Notes

This file is intentionally lightweight.
It should evolve over time as new sources appear, old sources become stale, and real workflow usage reveals which sources are actually useful.