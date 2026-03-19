import json
import os
import sys

def formalize_rules(rule_text):
    """
    将自然语言博弈规则转为结构化定义。
    此次针对狼人杀 9 人局（无警长：3狼, 1预, 1女, 1猎, 3民）。
    基于人类专家的反馈：狼人首夜并不知道谁是神职/平民，只有当白天有人起跳后才知道，
    或者有平民诈跳挡刀。因此，狼人的夜间动作应抽象为基于概率的盲刀或基于白天信息的追刀。
    这里将焦点放回【预言家 (P1)】与【狼人阵营 (P2)】的混合策略对抗上。
    """
    # 策略组合定义：
    # 预言家 (P1) 策略组合（考虑挡刀与起跳时机）：
    # - TrueJump_Day1: 预言家首日真跳报查验
    # - Hide_LetVillagerFake: 预言家隐忍，由平民诈跳预言家挡刀
    # - TrueJump_Day2: 预言家首日隐忍，第二日再跳
    
    # 狼人阵营 (P2) 策略组合（考虑悍跳与追刀选择）：
    # - BluffSeer_KillJumper: 悍跳预言家，夜间优先刀跳神职的人（容易中挡刀）
    # - BluffSeer_KillSilent: 悍跳预言家，夜间刀不发言/隐忍的人（找真预言家）
    # - LayLow_KillJumper: 全体倒钩，夜间优先刀跳神职的人
    
    formalized = {
        "players": ["Seer_Faction", "Wolf_Faction"],
        "action_space": {
            "Seer_Faction": [
                "TrueJump_Day1", 
                "Hide_LetVillagerFake", 
                "TrueJump_Day2"
            ],
            "Wolf_Faction": [
                "BluffSeer_KillJumper", 
                "BluffSeer_KillSilent", 
                "LayLow_KillJumper"
            ]
        },
        # 收益矩阵评估逻辑 (P1收益, P2收益)：
        # - 预言家首日真跳 (TrueJump_Day1) 遇狼人悍跳+刀起跳者 (BluffSeer_KillJumper)：预言家大概率活不过当晚，收益较低。
        # - 平民诈跳挡刀 (Hide_LetVillagerFake) 遇狼人刀起跳者 (KillJumper)：狼人刀错人（刀中平民），预言家存活收益极高。
        # - 预言家隐忍 (Hide) 遇狼人刀隐忍者 (KillSilent)：预言家直接被盲刀出局，狼人收益极高。
        "payoff_matrix": [
            # P1: TrueJump_Day1
            [[-5, 5], [5, -5], [8, -8]], 
            # P1: Hide_LetVillagerFake
            [[10, -10], [-8, 8], [6, -6]], 
            # P1: TrueJump_Day2
            [[0, 0], [-10, 10], [-2, 2]]      
        ],
        "assumptions": [
            "将信息不对称（狼人不知身份）纳入策略：狼人的刀法只能基于白天的起跳行为或盲刀", 
            "引入了平民诈跳挡刀策略以保护隐忍的预言家", 
            "矩阵为预言家阵营(包含挡刀平民)与狼人阵营的零和博弈"
        ]
    }
    return formalized

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <stage_1_input.json>")
        return

    input_path = sys.argv[1]
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = formalize_rules(data.get("rule_text", ""))
    
    output_path = "stage_1_output.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"Formalization complete. Output: {output_path}")

if __name__ == "__main__":
    main()
