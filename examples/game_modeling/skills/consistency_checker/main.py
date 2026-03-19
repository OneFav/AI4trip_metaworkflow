import json
import sys

def check_consistency(sim_results, solver_results, tolerance=0.1):
    """
    检查仿真结果（Stage 2）与数学求解（Stage 3）的一致性。
    """
    # 模拟一致性检查逻辑
    discrepancies = []
    is_consistent = True
    
    sim_eq = sim_results.get("equilibrium_candidates", [{}])[0]
    solver_eq = solver_results.get("equilibria", [{}])[0]
    
    # 此处为简化逻辑，对比 P1 策略首位概率
    sim_p1 = sim_eq.get("prob", 0)
    solver_p1 = solver_eq.get("P1_strategy", [0])[0]
    
    if abs(sim_p1 - solver_p1) > tolerance:
        is_consistent = False
        discrepancies.append({
            "field": "P1_strategy",
            "sim": sim_p1,
            "solver": solver_p1,
            "reason": "Simulation not yet converged or local optima"
        })
    
    return {
        "is_consistent": is_consistent,
        "discrepancies": discrepancies,
        "confidence_level": "High" if is_consistent else "Medium"
    }

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <stage_2_output.json> <stage_3_output.json>")
        return

    sim_path = sys.argv[1]
    solver_path = sys.argv[2]
    
    with open(sim_path, 'r', encoding='utf-8') as f:
        sim_results = json.load(f)
    with open(solver_path, 'r', encoding='utf-8') as f:
        solver_results = json.load(f)

    report = check_consistency(sim_results, solver_results)
    
    output_path = "consistency_report.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"Consistency check complete. Output: {output_path}")

if __name__ == "__main__":
    main()
