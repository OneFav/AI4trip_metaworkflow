---
name: "latex-helper"
description: "使用 LaTeX 生成专业文档、论文、报告。当用户提到：创建 LaTeX 文档、生成 PDF、排版学术论文、制作简历、生成公式、写报告、制作幻灯片（Beamer）时触发。"
---

# LaTeX Helper

本技能帮助用户使用 LaTeX 生成专业排版的文档。

## 何时使用

当用户提到以下场景时触发本技能：
- "帮我写一个 LaTeX 文档"
- "生成 PDF"
- "排版论文/报告/简历"
- "创建数学公式"
- "制作 Beamer 幻灯片"
- "写学术论文"

## LaTeX 基础结构

一个标准的 LaTeX 文档结构如下：

```latex
\documentclass[12pt, a4paper]{article}
\usepackage{ctex}                    % 中文支持
\usepackage{geometry}                % 页面设置
\geometry{margin=1in}
\usepackage{amsmath}                 % 数学公式
\usepackage{graphicx}                % 图片
\usepackage{hyperref}                % 超链接
\usepackage{listings}                % 代码块

\begin{document}

\title{文档标题}
\author{作者名}
\date{\today}

\maketitle

\section{第一节}
内容...

\end{document}
```

## 常用宏包

| 宏包 | 用途 |
|------|------|
| `ctex` | 中文支持 |
| `geometry` | 页面边距设置 |
| `amsmath` | 数学公式 |
| `graphicx` | 插入图片 |
| `hyperref` | 超链接与 PDF 书签 |
| `listings` / `minted` | 代码高亮 |
| `tikz` | 绘图 |
| `babel` | 多语言支持 |
| `fontspec` | 字体设置 |
| `xcolor` | 颜色支持 |

## 数学公式

### 行内公式
```latex
欧拉公式: $e^{i\pi} + 1 = 0$
```

### 独立公式
```latex
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 公式对齐
```latex
\begin{align}
a &= b + c \\
  &= d + e + f
\end{align}
```

## 图片插入

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.5\textwidth]{image.png}
\caption{图片标题}
\label{fig:example}
\end{figure}
```

## 代码块

使用 `listings` 宏包：

```latex
\lstset{
    backgroundcolor=\color{gray!10},
    basicstyle=\ttfamily\small,
    breaklines=true,
    frame=single,
}
\begin{lstlisting}[language=Python]
def hello():
    print("Hello, LaTeX!")
\end{lstlisting}
```

## 表格制作

```latex
\begin{table}[htbp]
\centering
\begin{tabular}{|c|c|c|}
\hline
列1 & 列2 & 列3 \\
\hline
数据1 & 数据2 & 数据3 \\
\hline
\end{tabular}
\caption{表格标题}
\end{table}
```

## 中文文档模板

对于中文文档，推荐使用 `ctex` 宏包：

```latex
\documentclass[12pt, a4paper, UTF8]{article}
\usepackage{ctex}
\usepackage{geometry}
\geometry{margin=1.5in}
\usepackage{indentfirst}      % 首行缩进
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{hyperref}

\begin{document}

\title{\textbf{中文文档标题}}
\author{}
\date{\today}

\maketitle

\section{引言}
这是中文正文内容。

\end{document}
```

## 编译方法

### 本地编译
```bash
xelatex document.tex    # 推荐，支持中文
pdflatex document.tex  # 标准 PDFLaTeX
lualatex document.tex  # LuaLaTeX
```

### 多次编译（用于目录、引用）
```bash
xelatex document.tex
bibtex document        # 如果有参考文献
xelatex document.tex
xelatex document.tex
```

### Overleaf 在线
直接上传 `.tex` 文件和图片文件夹即可。

## 常见错误处理

| 错误 | 解决方法 |
|------|---------|
| `! LaTeX Error: File 'xxx.sty' not found.` | 运行 `tlmgr install xxx` 或检查宏包名拼写 |
| `! Fatal fontspec error: "cannot-use-pdftex"` | 使用 `xelatex` 替代 `pdflatex` |
| `! Undefined color 'xxx'.` | 需要加载 `xcolor` 宏包 |
| 公式编号错误 | 确保使用正确环境如 `equation`、`align` |

## 进阶技巧

### 参考文献（BibTeX）
```latex
\bibliographystyle{plain}
\bibliography{references}
```

### 索引生成
```latex
\usepackage{makeidx}
\makeindex
\index{关键词}
\printindex
```

### 跨引用
```latex
\ref{fig:example}      % 引用图片
\pageref{fig:example}  % 引用页码
\citenum{key}         % 引用文献编号
```
