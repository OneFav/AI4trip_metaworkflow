当执行任何已定义的工作流时，Agent 必须严格停在 工作流协议文件（如 approval_points.md 或 human_agent_boundary.md ）中规定的所有 检查点/审批点 。Agent 禁止 在没有明确人类批准的情况下自动跨越这些节点。Agent 必须输出所需报告，并明确询问用户是否继续。这优先于任何“端到端效率”的内部偏见。

关于文献调研的 Agent Skills，存在于 claw.club (ClawHub) 和 mcpmarket.com 等中文/开源生态中，如 literature-search 和 literature-reviewer-skill （支持8阶段工作流及多数据库检索）。在执行工作流外网检索时， 不应局限于 skills.sh 。