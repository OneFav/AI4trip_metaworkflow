import sys
import json
import argparse
import traceback

def generate_pymc_template(model_spec, output_file):
    try:
        model_name = model_spec.get("model_name", "memory_attention_state_space")
        observed_acc = model_spec.get("observed_acc_column", "acc")
        observed_rt = model_spec.get("observed_rt_column", "rt")
        observed_i = model_spec.get("interference_column", "I")
        observed_d = model_spec.get("demand_column", "D")
        observed_u = model_spec.get("rehearsal_column", "U")
        observed_f = model_spec.get("fatigue_column", "F")
        draws = int(model_spec.get("draws", 1000))
        tune = int(model_spec.get("tune", 1000))

        template = f"""
import pymc as pm
import numpy as np
import pandas as pd

def zscore(v):
    v = np.asarray(v, dtype=float)
    s = np.std(v)
    if s == 0:
        return np.zeros_like(v)
    return (v - np.mean(v)) / s

def run_model(data_path, draws={draws}, tune={tune}):
    df = pd.read_csv(data_path)
    I = zscore(df["{observed_i}"].values)
    D = zscore(df["{observed_d}"].values)
    U = zscore(df["{observed_u}"].values)
    F = zscore(df["{observed_f}"].values)
    acc = df["{observed_acc}"].astype(int).values
    rt = np.asarray(df["{observed_rt}"].values, dtype=float)
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
"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(template)
            
        return {"status": "success", "message": f"Generated PyMC model template '{model_name}' at {output_file}"}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}

def main():
    parser = argparse.ArgumentParser(description="Generate Fallback PyMC Model Code")
    parser.add_argument("--spec", required=True, help="Path to JSON spec of the model")
    parser.add_argument("--output", required=True, help="Path to save the generated Python script")
    
    args = parser.parse_args()
    
    try:
        with open(args.spec, 'r', encoding='utf-8') as f:
            spec = json.load(f)
    except Exception as e:
        print(f"Error reading spec: {e}")
        sys.exit(1)
        
    result = generate_pymc_template(spec, args.output)
    
    if "error" in result:
        print(f"Error: {result['error']}")
        sys.exit(1)
    else:
        print(result["message"])

if __name__ == "__main__":
    main()
