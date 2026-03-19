description: "Fallback 版本的本地文献调研工具。当 claw.club 的 MCP 技能不可用时，通过 arXiv API 进行基础检索。"

---

# local_literature_search

A fallback python wrapper that searches the arXiv API for cognitive neuroscience literature if the primary MCP `literature-reviewer-skill` is unavailable.

## Usage

```bash
python main.py --query "attention memory trace" --output "results.json" --max_results 5
```
