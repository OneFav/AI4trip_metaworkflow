import json
import random
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from scipy.io import mmread
from scipy.stats import spearmanr
import ot


ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "test_run" / "realgw_artifacts"
ART.mkdir(parents=True, exist_ok=True)


def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def read_genes(path: Path) -> list[str]:
    genes = []
    for line in path.read_text(encoding="utf-8").splitlines():
        parts = line.strip().split("\t")
        genes.append(parts[0])
    return genes


def zscore(x: np.ndarray) -> np.ndarray:
    mu = x.mean(axis=0, keepdims=True)
    sd = x.std(axis=0, keepdims=True) + 1e-8
    return (x - mu) / sd


def cosine_delta(r: np.ndarray) -> np.ndarray:
    rn = r / (np.linalg.norm(r, axis=1, keepdims=True) + 1e-8)
    sim = rn @ rn.T
    return 1.0 - np.clip(sim, -1.0, 1.0)


def gw_distance(c1: np.ndarray, c2: np.ndarray) -> float:
    p = np.ones(c1.shape[0]) / c1.shape[0]
    q = np.ones(c2.shape[0]) / c2.shape[0]
    return float(ot.gromov.gromov_wasserstein2(c1, c2, p, q, "square_loss"))


def build_grn_response() -> tuple[np.ndarray, dict]:
    matrix_path = ROOT / "external_candidates" / "scanpy" / "tests" / "_data" / "10x_data" / "1.2.0" / "filtered_gene_bc_matrices" / "hg19_chr21" / "matrix.mtx"
    genes_path = ROOT / "external_candidates" / "scanpy" / "tests" / "_data" / "10x_data" / "1.2.0" / "filtered_gene_bc_matrices" / "hg19_chr21" / "genes.tsv"
    mat = mmread(matrix_path).tocsr()
    x = mat.T.toarray().astype(np.float32)
    genes = read_genes(genes_path)
    gene_to_idx = {g: i for i, g in enumerate(genes)}
    selected = ["RUNX1", "ETS2", "ERG", "IFNAR1", "IFNAR2", "IL10RB", "RCAN1", "SOD1", "CBS", "BACH1"]
    idx = [gene_to_idx[g] for g in selected if g in gene_to_idx]
    x_sel = np.log1p(x[:, idx])
    x_sel = zscore(x_sel)
    sel_to_i = {g: i for i, g in enumerate([g for g in selected if g in gene_to_idx])}
    runx1 = x_sel[:, sel_to_i["RUNX1"]]
    ifnar = np.mean([x_sel[:, sel_to_i["IFNAR1"]], x_sel[:, sel_to_i["IFNAR2"]], x_sel[:, sel_to_i["IL10RB"]]], axis=0)
    stress = np.mean([x_sel[:, sel_to_i["RCAN1"]], x_sel[:, sel_to_i["SOD1"]], x_sel[:, sel_to_i["CBS"]]], axis=0)
    q80_r = np.quantile(runx1, 0.8)
    q80_i = np.quantile(ifnar, 0.8)
    q80_s = np.quantile(stress, 0.8)
    q40_r = np.quantile(runx1, 0.4)
    q60_r = np.quantile(runx1, 0.6)
    n = x_sel.shape[0]
    masks = []
    rng = np.random.default_rng(42)
    baseline_idx = rng.choice(np.arange(n), size=max(10, n // 5), replace=False)
    m1 = np.zeros(n, dtype=bool)
    m1[baseline_idx] = True
    masks.append(m1)
    masks.append(runx1 >= q80_r)
    masks.append(ifnar >= q80_i)
    masks.append(stress >= q80_s)
    conflict = (runx1 >= q80_r) & (stress >= q80_s)
    if conflict.sum() < 10:
        conflict = (runx1 >= q80_r) | (stress >= q80_s)
    masks.append(conflict)
    masks.append((runx1 >= q40_r) & (runx1 <= q60_r))
    modules = {
        "switch_core": ["RUNX1", "ETS2", "ERG"],
        "immune_gate": ["IFNAR1", "IFNAR2", "IL10RB"],
        "stress_reg": ["RCAN1", "SOD1", "CBS"],
        "homeostasis": ["BACH1", "CBS", "SOD1"]
    }
    r = []
    for m in masks:
        row = []
        for gs in modules.values():
            cols = [sel_to_i[g] for g in gs if g in sel_to_i]
            row.append(float(x_sel[m][:, cols].mean()))
        r.append(row)
    r = np.array(r, dtype=np.float64)
    meta = {"cells": int(n), "genes_used": [g for g in selected if g in gene_to_idx]}
    return r, meta


def build_prototype_responses() -> dict[str, np.ndarray]:
    r_switch = np.array([
        [0.2, 0.2, 0.2, 0.2],
        [0.9, 0.3, 0.2, 0.4],
        [0.3, 0.9, 0.2, 0.4],
        [0.2, 0.3, 0.9, 0.5],
        [0.8, 0.2, 0.8, 0.3],
        [0.4, 0.4, 0.4, 0.7]
    ], dtype=np.float64)
    r_memory = np.array([
        [0.3, 0.3, 0.3, 0.6],
        [0.5, 0.4, 0.3, 0.7],
        [0.6, 0.5, 0.4, 0.8],
        [0.7, 0.5, 0.4, 0.8],
        [0.7, 0.6, 0.4, 0.9],
        [0.8, 0.6, 0.5, 0.9]
    ], dtype=np.float64)
    r_local = np.array([
        [0.4, 0.2, 0.2, 0.3],
        [0.5, 0.25, 0.2, 0.35],
        [0.45, 0.3, 0.22, 0.37],
        [0.42, 0.35, 0.24, 0.4],
        [0.4, 0.4, 0.25, 0.42],
        [0.38, 0.45, 0.26, 0.43]
    ], dtype=np.float64)
    return {"Proto-Switch": r_switch, "Proto-Memory": r_memory, "Proto-Local": r_local}


class GRUModel(nn.Module):
    def __init__(self, hidden: int = 16):
        super().__init__()
        self.gru = nn.GRU(input_size=2, hidden_size=hidden, batch_first=True)
        self.head = nn.Linear(hidden, 1)

    def forward(self, x):
        h, _ = self.gru(x)
        y = self.head(h)
        return y, h


class MLPModel(nn.Module):
    def __init__(self, hidden: int = 16):
        super().__init__()
        self.ff = nn.Sequential(nn.Linear(2, hidden), nn.Tanh(), nn.Linear(hidden, 1))
        self.hidden = hidden

    def forward(self, x):
        b, t, _ = x.shape
        xf = x.reshape(b * t, -1)
        h = torch.tanh(self.ff[0](xf))
        y = self.ff[2](h).reshape(b, t, 1)
        h = h.reshape(b, t, self.hidden)
        return y, h


class SSMModel(nn.Module):
    def __init__(self, hidden: int = 16):
        super().__init__()
        self.a = nn.Parameter(torch.eye(hidden) * 0.9)
        self.b = nn.Parameter(torch.randn(2, hidden) * 0.1)
        self.c = nn.Parameter(torch.randn(hidden, 1) * 0.1)
        self.hidden = hidden

    def forward(self, x):
        b, t, _ = x.shape
        h = torch.zeros(b, self.hidden, device=x.device)
        hs = []
        ys = []
        for i in range(t):
            h = torch.tanh(h @ self.a + x[:, i, :] @ self.b)
            y = h @ self.c
            hs.append(h.unsqueeze(1))
            ys.append(y.unsqueeze(1))
        return torch.cat(ys, dim=1), torch.cat(hs, dim=1)


class MoEModel(nn.Module):
    def __init__(self, hidden: int = 16):
        super().__init__()
        self.e1 = nn.Linear(2, hidden)
        self.e2 = nn.Linear(2, hidden)
        self.gate = nn.Linear(2, 2)
        self.out = nn.Linear(hidden, 1)

    def forward(self, x):
        b, t, _ = x.shape
        xf = x.reshape(b * t, -1)
        g = torch.softmax(self.gate(xf), dim=-1)
        h1 = torch.tanh(self.e1(xf))
        h2 = torch.tanh(self.e2(xf))
        h = g[:, :1] * h1 + g[:, 1:] * h2
        y = self.out(h).reshape(b, t, 1)
        return y, h.reshape(b, t, -1)


def make_switch_batch(batch: int, length: int, switch_p: float, noise: float) -> tuple[torch.Tensor, torch.Tensor]:
    x = np.random.randn(batch, length, 1).astype(np.float32)
    rule = np.zeros((batch, length, 1), dtype=np.float32)
    for b in range(batch):
        state = 0.0
        for t in range(length):
            if np.random.rand() < switch_p:
                state = 1.0 - state
            rule[b, t, 0] = state
    cue = rule + np.random.randn(batch, length, 1).astype(np.float32) * noise
    y = np.where(rule > 0.5, -x, x)
    inp = np.concatenate([x, cue], axis=-1)
    return torch.tensor(inp), torch.tensor(y)


def train_model(model: nn.Module, steps: int = 180) -> float:
    opt = optim.Adam(model.parameters(), lr=1e-2)
    loss_fn = nn.MSELoss()
    model.train()
    for _ in range(steps):
        xb, yb = make_switch_batch(48, 24, switch_p=0.2, noise=0.15)
        pred, _ = model(xb)
        loss = loss_fn(pred, yb)
        opt.zero_grad()
        loss.backward()
        opt.step()
    model.eval()
    x_val, y_val = make_switch_batch(96, 24, switch_p=0.2, noise=0.15)
    with torch.no_grad():
        pred, _ = model(x_val)
        mse = float(loss_fn(pred, y_val).item())
    return mse


def ann_response(model: nn.Module) -> np.ndarray:
    probe_cfg = [
        (0.05, 0.05),
        (0.10, 0.10),
        (0.20, 0.15),
        (0.30, 0.20),
        (0.35, 0.30),
        (0.15, 0.05)
    ]
    rows = []
    model.eval()
    for sp, nz in probe_cfg:
        xb, _ = make_switch_batch(64, 24, switch_p=sp, noise=nz)
        with torch.no_grad():
            _, h = model(xb)
            v = h.mean(dim=(0, 1)).cpu().numpy()
        rows.append(v)
    return np.array(rows, dtype=np.float64)


def main() -> None:
    set_seed(42)
    r_grn, grn_meta = build_grn_response()
    delta_grn = cosine_delta(r_grn)
    protos = build_prototype_responses()
    proto_scores = {}
    for name, r in protos.items():
        proto_scores[name] = gw_distance(delta_grn, cosine_delta(r))
    topk = sorted(proto_scores.items(), key=lambda x: x[1])
    topk_payload = {
        "grn_chr21_real_expression": [{"prototype": k, "score": float(v)} for k, v in topk],
        "distance_summary": {"metric": "GW", "cells": grn_meta["cells"], "genes_used": grn_meta["genes_used"]}
    }
    (ART / "topk_task_prototypes_realgw.json").write_text(json.dumps(topk_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    models = {
        "gru": GRUModel(),
        "ssm": SSMModel(),
        "moe": MoEModel(),
        "sparse_mlp": MLPModel()
    }
    mse_scores = {}
    ann_dist = {}
    for name, m in models.items():
        mse_scores[name] = train_model(m)
        r_ann = ann_response(m)
        ann_dist[name] = gw_distance(delta_grn, cosine_delta(r_ann))
    ranked = sorted(ann_dist.items(), key=lambda x: x[1])
    ranked_payload = {
        "grn_chr21_real_expression": {
            topk[0][0]: [{"ann": n, "score": float(s), "mse": float(mse_scores[n])} for n, s in ranked]
        }
    }
    (ART / "ranked_ann_results_realgw.json").write_text(json.dumps(ranked_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    dist_values = np.array([s for _, s in ranked], dtype=np.float64)
    mse_values = np.array([mse_scores[n] for n, _ in ranked], dtype=np.float64)
    corr = float(spearmanr(dist_values, mse_values).correlation)
    judgement = "preliminary_supported" if corr >= 0.2 else "preliminary_inconclusive"
    report = [
        "# Validation Report (Real GW + Real Expression)",
        "",
        f"- input_cells: {grn_meta['cells']}",
        f"- genes_used: {', '.join(grn_meta['genes_used'])}",
        f"- top_prototype: {topk[0][0]} ({topk[0][1]:.4f})",
        f"- ann_best: {ranked[0][0]} (gw={ranked[0][1]:.4f}, mse={mse_scores[ranked[0][0]]:.4f})",
        f"- distance/performance rank consistency (spearman): {corr:.3f}",
        f"- judgement: {judgement}"
    ]
    (ART / "validation_report_realgw.md").write_text("\n".join(report), encoding="utf-8")

    summary = {
        "status": "completed",
        "input": "scanpy 10x hg19_chr21 matrix.mtx",
        "topk_file": str(ART / "topk_task_prototypes_realgw.json"),
        "ranked_ann_file": str(ART / "ranked_ann_results_realgw.json"),
        "validation_report": str(ART / "validation_report_realgw.md"),
        "top_prototype": topk[0][0],
        "best_ann": ranked[0][0]
    }
    (ART / "workflow_realgw_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
