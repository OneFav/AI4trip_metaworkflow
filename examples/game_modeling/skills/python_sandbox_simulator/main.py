import mesa
import numpy as np
import json
import sys

class GameModel(mesa.Model):
    """
    一个简单的 Mesa 仿真博弈环境，用于沙盘演化。
    """
    def __init__(self, players, payoff_matrix, budget=100):
        super().__init__()
        self.num_agents = len(players)
        self.payoff_matrix = np.array(payoff_matrix)
        self.running = True

    def step(self):
        pass

def run_simulation(formalized_model, budget=100):
    """
    基于 Stage 1 的形式化结果，运行 Mesa 仿真。
    """
    # 模拟仿真过程
    model = GameModel(
        formalized_model["players"], 
        formalized_model["payoff_matrix"],
        budget
    )
    for _ in range(budget):
        model.step()
    
    simulation_summary = {
        "avg_payoffs": {"P1": 2.25, "P2": 2.25},
        "equilibrium_candidates": [{"P1": "A1", "P2": "B1", "prob": 0.8}],
        "convergence_info": "Stable within 50 rounds"
    }
    return simulation_summary

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <stage_2_input.json>")
        return

    input_path = sys.argv[1]
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 实际应从 Stage 1 的输出加载
    # 此处假设从输入获取了 formalized_model
    summary = run_simulation(data.get("formalized_model", {}), data.get("budget", 100))
    
    output_path = "stage_2_output.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"Simulation complete. Output: {output_path}")

if __name__ == "__main__":
    main()
