import nashpy as nash
import numpy as np
import json
import sys

def solve_equilibrium(payoff_matrix):
    """
    使用 Nashpy 求解博弈均衡。
    """
    # 转换为 Nashpy 输入
    A = np.array(payoff_matrix)[:, :, 0]
    B = np.array(payoff_matrix)[:, :, 1]
    game = nash.Game(A, B)
    
    # 求解 Lemke-Howson 均衡
    equilibria = list(game.lemke_howson_enumeration())
    
    # 格式化输出
    eq_results = []
    for eq in equilibria:
        eq_results.append({
            "P1_strategy": eq[0].tolist(),
            "P2_strategy": eq[1].tolist(),
            "payoffs": game[eq].tolist()
        })
    return eq_results

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <stage_3_input.json>")
        return

    input_path = sys.argv[1]
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 实际应从 Stage 1 的输出加载
    payoff_matrix = data.get("payoff_matrix", [[[3, 3], [0, 5]], [[5, 0], [1, 1]]])
    equilibria = solve_equilibrium(payoff_matrix)
    
    output_path = "stage_3_output.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({"equilibria": equilibria}, f, ensure_ascii=False, indent=2)
    print(f"Equilibrium solving complete. Output: {output_path}")

if __name__ == "__main__":
    main()
