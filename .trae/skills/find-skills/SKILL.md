
description: "外部技能发现层。当本地 guidebook (skill_registry / skill_sources) 无法满足需求时，或者需要检索具体的外部 skill repo 列表时，调用此技能进行外网生态检索。"

---

# Find Skills

This skill helps you discover and retrieve candidates from the open agent skills ecosystem.

## When to Use This Skill
Use this skill when:
- The `workflow_solver` needs to find external capabilities that are not covered by `skill_registry.md` or `skill_sources.md`.
- You need to search a skill directory (like Awesome Skills).
- You want to list skills within a specific known repository (e.g., `anthropics/skills`, `vercel-labs/agent-skills`).

## Execution Logic in Meta-Workflow

When `01_workflow_solver` is looking for skills, it MUST follow this priority:
1. **Check `guides/skill_registry.md`** (Fast path for known good local references).
2. **Check `guides/skill_sources.md`** (Fast path for known repos).
3. **Invoke `find-skills` (This tool)** to search the external ecosystem.

Inside `find-skills`, follow this search priority:
1. **Directory Search**: Search broader directory sites and registries, including:
   - `claw.club` (ClawHub / Claude Code Skills - especially for Chinese-supported workflows)
   - Awesome Skills (`https://www.awesomeskills.dev/`)
   - `skills.sh` leaderboard
   - MCP Market (`mcpmarket.com`, `fastmcp.me`)
   This acts as a map for initial filtering. Do not restrict your search to just one site.
2. **Repo List**: If you identify a specific skill repo (e.g., `anthropics/skills`, `VoltAgent/awesome-openclaw-skills`), use equivalent API/Web searches to list its internal capabilities.
3. **Write Candidates**: DO NOT auto-install. Extract the relevant skill candidates, format them, and return them to the `workflow_solver` to be written into the `workflow_plan.md` under `External Search Verification`.

## Command Reference (Simulated for Meta-Workflow)

You can use the underlying CLI commands to fetch info (or simulate them via WebSearch if CLI is unavailable):
- `npx skills find [query]` - Search for skills by keyword.
- `npx skills add <package> --list` - (Conceptual) List skills inside a specific package/repo.

## Output Contract
Return a structured list of candidates:
```markdown
### Verified Candidate X
* capability: [what it does]
* candidate_project: [repo/skill name]
* source_url: [url]
* verification_summary: [why it fits]
* install_command: [e.g., npx skills add ...]
* action: DO NOT INSTALL YET. Write to plan.
```