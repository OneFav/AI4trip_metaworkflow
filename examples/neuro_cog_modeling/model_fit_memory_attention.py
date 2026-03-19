
import pymc as pm
import numpy as np
import pandas as pd

def zscore(v):
    v = np.asarray(v, dtype=float)
    s = np.std(v)
    if s == 0:
        return np.zeros_like(v)
    return (v - np.mean(v)) / s

def run_model(data_path, draws=1000, tune=1000):
    df = pd.read_csv(data_path)
    I = zscore(df["I"].values)
    D = zscore(df["D"].values)
    U = zscore(df["U"].values)
    F = zscore(df["F"].values)
    acc = df["acc"].astype(int).values
    rt = np.asarray(df["rt"].values, dtype=float)
    n = len(df)

    with pm.Model() as model:
        alpha_M = pm.Beta("alpha_M", alpha=8, beta=2)
        alpha_A = pm.Beta("alpha_A", alpha=8, beta=2)
        beta_M = pm.HalfNormal("beta_M", sigma=1.0)
        delta_A = pm.HalfNormal("delta_A", sigma=1.0)
        gamma_M = pm.HalfNormal("gamma_M", sigma=1.0)
        eta_A = pm.HalfNormal("eta_A", sigma=1.0)
        phi_A = pm.HalfNormal("phi_A", sigma=1.0)
        kappa_M = pm.HalfNormal("kappa_M", sigma=1.0)

        w0 = pm.Normal("w0", mu=0.0, sigma=1.5)
        w1 = pm.Normal("w1", mu=0.0, sigma=1.0)
        w2 = pm.Normal("w2", mu=0.0, sigma=1.0)
        w3 = pm.Normal("w3", mu=0.0, sigma=1.0)

        r0 = pm.Normal("r0", mu=0.0, sigma=1.0)
        c1 = pm.HalfNormal("c1", sigma=1.0)
        c2 = pm.HalfNormal("c2", sigma=1.0)
        c3 = pm.HalfNormal("c3", sigma=1.0)

        sigma_M = pm.HalfNormal("sigma_M", sigma=1.0)
        sigma_A = pm.HalfNormal("sigma_A", sigma=1.0)
        sigma_rt = pm.HalfNormal("sigma_rt", sigma=1.0)

        M = pm.Normal("M", mu=0.0, sigma=1.0, shape=n)
        A = pm.Normal("A", mu=0.0, sigma=1.0, shape=n)

        mu_M = alpha_M * pm.math.concatenate([[0], M[:-1]]) + beta_M * pm.math.concatenate([[0], A[:-1]]) - gamma_M * I + kappa_M * pm.math.concatenate([[0], A[:-1]]) * U
        mu_A = alpha_A * pm.math.concatenate([[0], A[:-1]]) + delta_A * D - eta_A * I - phi_A * F

        pm.Normal("M_dyn", mu=mu_M, sigma=sigma_M, observed=M)
        pm.Normal("A_dyn", mu=mu_A, sigma=sigma_A, observed=A)

        p_acc = pm.math.sigmoid(w0 + w1 * M + w2 * A + w3 * M * A)
        pm.Bernoulli("acc_obs", p=p_acc, observed=acc)

        mu_rt = r0 - c1 * M - c2 * A + c3 * I
        pm.LogNormal("rt_obs", mu=mu_rt, sigma=sigma_rt, observed=np.clip(rt, 1e-4, None))

        idata = pm.sample(draws=draws, tune=tune, target_accept=0.9, chains=2, cores=1)
    return idata

if __name__ == "__main__":
    run_model("data.csv")
