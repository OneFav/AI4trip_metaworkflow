# Intent

## Meta

* workflow_name: neuro_cog_modeling
* created_at: 2026-03-18
* status: intent_defined

## Goal

针对认知神经科学领域中“两个相关现象/机制”（1+1），提出统一的数学模型（如漂移扩散模型 DDM、贝叶斯推断、强化学习模型或神经网络等），并利用计算框架拟合人类行为/神经数据，验证该模型的统一解释力。

## Scene

该 workflow 主要用于科研初期的探索与建模（desk/research 场景）。适用于计算神经科学、认知心理学研究者在获得文献或初步数据后，快速构建“桥接理论”并跑通初步拟合实验。

## Design Intent

科学研究中往往面临大量孤立现象，本工作流的核心理念是“统一与计算”。它致力于将“口头上的相关性猜测”转化为“可计算、可拟合参数的数学模型”，帮助研究者快速淘汰不合理的假设，加速从 idea 到 protocol 的进程。

## Human-Agent Boundary

### Human

* 提出两个具体的认知/神经现象（如“注意捕获”与“工作记忆容量”）。
* 提供相关的实证数据（或数据分布特征）用于拟合。
* 评估最终模型是否在生物学/心理学意义上合理（Biological Plausibility）。
* **提出 2-3 个反例场景（Counter-examples/Challenge Cases）来质疑当前模型，迫使模型解释或修正。**

### Agent

* **针对两个目标现象执行文献调研（Literature Review），梳理现有理论解释与关键参数。**
* 检索与综合现有的计算框架（如 DDM, RL, 贝叶斯等）。
* 提出 2-3 个能统合这两个现象的数学模型候选。
* 针对人类提出的质疑场景，尝试调整模型结构或参数以给出回应（Response to Challenge）。
* 编写模型代码，执行参数搜索与数据拟合。
* 比较模型拟合优度（AIC/BIC 等），生成分析报告。

### Human-Agent

* 共同讨论并决定采用哪种基础数学框架（例如：决定用 RL 还是 DDM）。
* **进行“质疑-辩护”对话，确认模型在边缘情况下的鲁棒性。**
* 共同解读参数拟合结果，讨论是否需要增加模型复杂度。

## Candidate Checkpoints

1. **checkpoint_model_proposal**: Agent 提出 2-3 种数学建模框架后，停止执行，向人类汇报各模型的假设与优缺点；人类决策选择哪一个框架进入编码与拟合阶段。
2. **checkpoint_challenge_response**: 在选定框架后，人类必须提出 2-3 个反例场景（Challenge Cases），Agent 必须尝试解释或修正模型以回应质疑。只有当人类认可回应后，才允许进入大规模数据拟合。
3. **checkpoint_fit_evaluation**: Agent 完成初步拟合后，汇报拟合优度与参数解释；人类决定是结束工作流、调整参数，还是换用另一个数学模型。

## Automation Preference

* mode: balanced
* reason: 数学模型的选择需要强烈的领域知识与直觉判断，不能全权交给 Agent 盲目计算。但编写拟合代码和计算 AIC/BIC 等重复性劳动应高度自动化。

## Trip/Mobile Orientation

* trip_compatible: partial
* mobile_friendly: partial
* notes: 提出现象、审核模型设计思路完全可以在手机/旅途中通过聊天完成；但大规模的数据拟合与参数搜索必须交由后台 Agent 在桌面/服务器端运行，并将图表结果发送至移动端供人类审查。

## Notes for Skill 2

在设计阶段和寻找外部技能时，必须优先考虑具有成熟认知建模库的生态（例如 Python 中的 `HDDM`, `PyMC`, 或是强化学习环境）。输入必须明确包含两个现象的描述，输出必须有量化的拟合指标。
