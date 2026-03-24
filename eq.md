# GRN→任务原型→ANN验证：自动化工作流 v1

## 0. 目标

输入一个或多个候选 GRN（或 GRN 模块），自动化完成：

1. 将 GRN 转成统一可比较的“观测几何对象”；
2. 在一个受约束的任务原型库中，自动生成/筛选最匹配的任务原型；
3. 用统一探针协议测量候选 ANN；
4. 计算 GRN—任务原型—ANN 三者距离；
5. 用外部实验验证“距离近 → 更适合该任务原型”的结论是否靠谱。

---

## 1. 核心原则

### 原则 P1：不做开放世界“GRN→任意任务”生成

系统不直接从 GRN 自由生成无限任务，而是在**固定任务原型库**内做排序、筛选、参数化。

### 原则 P2：不直接比较原始神经元激活和基因表达

统一先经过同一类观测逻辑，构造“探针诱导的观测几何对象”。

### 原则 P3：核心对象只有一个

核心比较对象统一为：

**Probe-Induced Response Geometry（PIRG）**

即：在统一探针协议下，系统对不同条件的群体响应所诱导出的几何/关系结构。

### 原则 P4：任务原型不是人工语义标签，而是“成功解决该任务的模型群体”诱导出的代表性几何对象。

### 原则 P5：输出的是“带置信度的 Top-K 匹配假设”，不是绝对真理。

### 原则 P6：所有结论必须经过外部验证，而不是只看距离本身。

---

## 2. 总体架构

```text
GRN输入
  ↓
GRN预处理与模块化
  ↓
统一探针协议编译器
  ↓
GRN响应采集/模拟
  ↓
PIRG构造器
  ↓
任务原型库匹配器
  ↓
Top-K任务原型
  ↓
候选ANN统一测量
  ↓
GRN-PIRG 与 ANN-PIRG 距离排序
  ↓
外部任务验证与报告
```

---

## 3. 输入与输出

## 3.1 输入

### A. 生物侧输入

* 一个或多个 GRN / GRN 模块
* 可选：调控边权、节点注释、模块标签、扰动响应数据、时间序列表达
* 可选：预先整理好的 regulon / pathway / module 活性

### B. 任务原型库

不是自由任务，而是一个有限集合，例如：

* Proto-Memory：部分可观测记忆原型
* Proto-Switch：上下文切换/门控原型
* Proto-Local：局部传播/搜索原型
* Proto-Attractor：多稳态/状态保持原型
* Proto-Integrate：证据整合/慢思维原型

### C. ANN 候选集

例如：

* Sparse/Modular MLP
* RNN/GRU/LSTM
* SSM
* MoE
* Attractor-like recurrent net

### D. 统一探针协议模板库

每个任务原型带一个 probe family。

## 3.2 输出

* 每个 GRN 的 Top-K 任务原型匹配结果
* 每个任务原型下 ANN 家族距离排序
* “最近 ANN 是否更适合该任务原型”的验证结果
* 报告：稳定性、显著性、失败案例、结论可信度

---

## 4. 核心对象：PIRG

## 4.1 定义

对任意系统 S（GRN 或 ANN），给定统一探针协议 (\mathcal P = {u_1,\dots,u_m})，得到群体响应矩阵：

[
R_S \in \mathbb{R}^{m \times d_S}
]

其中：

* (m)：probe 条件数
* (d_S)：该系统的观测维度（ANN 可是 hidden/state 维度；GRN 可是 module/regulon 维度）

然后构造 probe 间关系矩阵：

[
K_S(i,j) = \mathrm{sim}(R_S(i,:), R_S(j,:))
]

或其距离版本：

[
\Delta_S(i,j) = 1 - K_S(i,j)
]

把 ((\mathcal U, \Delta_S)) 视为系统 S 的 PIRG。

## 4.2 好处

* 不要求 GRN 和 ANN 有相同维度；
* 不要求神经元与基因一一对应；
* 对单元重排和维度差异更鲁棒；
* 能作为整个工作流的唯一核心对象。

---

## 5. 自动化工作流分阶段

## 阶段 A：任务原型库构建（离线）

### A1. 固定任务原型模板

先手工固定一个小库，不做开放世界：

* Proto-Memory
* Proto-Switch
* Proto-Local
* Proto-Attractor
* Proto-Integrate

### A2. 为每个任务原型定义统一 probe family

例如：

* Memory：遮挡长度、延迟长度、部分观测比例
* Switch：上下文翻转、规则切换频率、门控冲突程度
* Local：局部扰动半径、障碍密度、邻域传播深度
* Attractor：初值扰动强度、噪声水平、模式缺损程度
* Integrate：证据强度、噪声方差、整合窗口长度

### A3. 为每个任务原型训练或收集 ANN 原型组

每个任务原型选 3–5 个成功模型组成原型组。

### A4. 测量 ANN 原型组，构造任务原型 PIRG

对每个模型：

1. 输入统一 probe family；
2. 读取统一层/状态；
3. 构造 PIRG；
4. 聚合为该任务原型的代表性 PIRG。

输出：

* `prototype_memory.pirg`
* `prototype_switch.pirg`
* `prototype_local.pirg`
* ...

### A5. 原型聚合策略

可用：

* 中位 PIRG
* Wasserstein barycenter
* 几何中位数

推荐默认：**几何中位 PIRG**。

---

## 阶段 B：GRN 侧自动测量

### B1. GRN 预处理

输入原始 GRN 后：

1. 去噪/标准化；
2. 模块化；
3. 选定观测层级：

   * regulon activity
   * pathway score
   * module activity
   * perturbation response vector

默认建议：**module/regulon 层级**，不直接用全基因表达。

### B2. 条件映射器

每个任务原型的 probe family，需映射到 GRN 可实现的条件族。

例如：

* Memory probe 中“延迟长度” → 生物侧“采样时间点/滞后窗口”
* Switch probe 中“上下文翻转” → 生物侧“刺激条件切换/扰动状态切换”
* Local probe 中“局部扰动半径” → 生物侧“局部模块 perturbation 的覆盖范围”

这一层不要求物理输入相同，只要求条件语义同构。

### B3. 响应采集

对每个映射后的条件：

* 如果有真实时间序列/扰动数据，直接读；
* 如果只有网络结构，则通过 GRN 动力学模拟器生成响应；
* 如果两者都不够，就只做结构层 surrogate，不进入主验证。

### B4. 构造 GRN-PIRG

和 ANN 完全相同：
[
R_M \rightarrow K_M \rightarrow \Delta_M
]
输出：

* `grn_X.pirg`

---

## 阶段 C：GRN → 任务原型匹配

### C1. 距离定义

主距离只用一种：

**PIRG 间的跨度量空间距离**

若两边维度和节点数不一致，优先用：

* Gromov–Wasserstein

若已经对齐到同一 probe 集，可用：

* Frobenius norm / kernel alignment / rank correlation

默认主距离：**GW 距离**。

### C2. 输出 Top-K 任务原型

对每个 GRN：
[
\tau^*(M) = \arg\min_{\tau \in \mathcal T_{cand}} D(\mathrm{PIRG}*M, \mathrm{PIRG}*\tau^*)
]

并输出：

* Top-1 任务原型
* Top-3 排名
* 距离间隔 margin
* bootstrap 置信区间

### C3. 任务原型参数化

对匹配到的任务原型，不仅给任务类别，还可自动细化参数：

* Memory 原型：推荐延迟长度范围
* Switch 原型：推荐切换频率范围
* Local 原型：推荐局部传播深度/地图尺寸

这一步相当于“带原则的生成任务原型”。

---

## 阶段 D：ANN 候选集统一测试

### D1. 对候选 ANN 家族统一训练/加载

对于匹配到的 Top-K 任务原型，准备候选 ANN：

* Sparse MLP
* RNN/GRU
* SSM
* MoE
* Attractor-like recurrent net

### D2. 统一 probe 测量

对每个 ANN：

1. 在该任务原型上训练到基本收敛；
2. 用同一 probe family 测量内部状态；
3. 构造 ANN-PIRG。

### D3. 距离排序

计算：
[
D(\mathrm{PIRG}*M, \mathrm{PIRG}*{N_i})
]
得到 ANN 排序。

输出：

* `ranked_ann_for_grn_X_under_proto_Y.json`

---

## 阶段 E：外部验证

这是最关键的一步。

### E1. 验证命题

要验证的不是“距离好看”，而是：

> 对于某个 GRN，距离最近的任务原型和距离最近的 ANN 家族，是否真的更适合承载该 GRN 所蕴含的计算约束？

### E2. 验证方式

#### 验证 1：性能相关性

如果某 ANN 与 GRN-PIRG 距离更近，它是否在匹配任务原型上表现更好？
指标包括：

* 初始性能
* 样本效率
* OOD 泛化
* 稳定性

#### 验证 2：排序一致性

如果距离排序为：
[
N_1 < N_2 < N_3
]
是否也大致满足：
[
\text{performance}(N_1) > \text{performance}(N_2) > \text{performance}(N_3)
]

#### 验证 3：消融与负对照

必须包含：

* 打乱 GRN 模块
* 度分布保留但边重连
* 随机 task prototype
* 随机 probe family

#### 验证 4：重采样稳定性

* probe bootstrap
* 条件子集重采样
* 模块子集重采样

如果 Top-K 排名对这些扰动稳定，结论才更可信。

---

## 6. 自动化模块清单

### 模块 M1：GRN Intake

* 读取 GRN / module graph / regulon matrix
* 统一 schema

### 模块 M2：Task Prototype Library Builder

* 管理任务原型模板、probe family、ANN 原型组、prototype PIRG

### 模块 M3：Probe Compiler

* 编译任务条件
* 映射到 ANN 输入与 GRN 条件

### 模块 M4：Observer

* ANN observer：读 hidden state / layer activation
* GRN observer：读 module/regulon activity / perturbation response

### 模块 M5：PIRG Builder

* 响应矩阵 → 相似度矩阵 / 几何对象

### 模块 M6：Distance Engine

* GW / Frobenius / rank corr

### 模块 M7：ANN Runner

* 训练/加载候选 ANN
* 统一 probe 测量

### 模块 M8：Validator

* 相关性检验
* 排序一致性
* 消融
* bootstrap

### 模块 M9：Reporter

* 自动生成结果表、失败案例、置信度说明

---

## 7. 推荐目录结构

```text
grn_taskproto_pipeline/
  configs/
    task_prototypes/
    probes/
    ann_families/
    distance/
  data/
    grn/
    ann_cache/
    prototype_library/
  src/
    grn/
      intake.py
      module_extractor.py
      observer.py
    ann/
      runners/
      observers/
    prototypes/
      build_library.py
      aggregate_pirg.py
    probes/
      compile_probe.py
      condition_mapper.py
    geometry/
      build_pirg.py
      distance.py
    validation/
      rank_correlation.py
      bootstrap.py
      ablation.py
    reports/
      make_report.py
  outputs/
    pirg/
    rankings/
    reports/
```

---

## 8. 第一版最小可行闭环（MVP）

### 任务原型库只保留 3 类

* Proto-Memory
* Proto-Switch
* Proto-Local

### GRN 只用模块级输入

* module activity / regulon score

### PIRG 只用一种形式

* probe-probe 相似度矩阵

### 距离只用一种主指标

* GW 距离

### ANN 家族只测 4 类

* Sparse MLP
* RNN/GRU
* SSM
* MoE

### 外部验证只做 3 项

* 样本效率
* OOD
* 排序一致性

---

## 9. 你最终要输出的不是“绝对对应”，而是“带置信度的结构化假设”

对每个输入 GRN，系统应输出类似：

```text
GRN-07
Top task prototypes:
1. Proto-Memory   score=0.18   CI=[0.16,0.21]
2. Proto-Switch   score=0.31   CI=[0.28,0.35]
3. Proto-Local    score=0.44   CI=[0.41,0.49]

Best ANN families under Proto-Memory:
1. GRU            score=0.20
2. SSM            score=0.27
3. MoE            score=0.36
4. Sparse MLP     score=0.48

Validation:
- sample efficiency rank corr = 0.72
- OOD rank corr = 0.64
- shuffled-GRN control failed
Conclusion:
- hypothesis supported (moderate confidence)
```

---

## 10. 最重要的边界

### 这套系统能做什么

* 给出“GRN 更像哪类任务原型”的有原则假设；
* 给出“哪类 ANN 更接近该 GRN”的排序；
* 用外部验证检查这种排序是否真的有任务意义。

### 这套系统不能直接声称什么

* 不能直接声称某个 GRN “本质上就是某个任务”；
* 不能直接声称最近 ANN 就等同于真实生物机制；
* 不能绕过真实实验与消融验证。

---

## 11. 一句话总结

这套自动化工作流的核心不是“从 GRN 生造任务”，而是：

> 先建立一个受约束的任务原型库；再用统一探针协议把 GRN 和 ANN 都映射成同一种观测几何对象 PIRG；最后通过距离排序和外部验证，判断“GRN → 任务原型 → ANN 家族”的匹配是否成立。
