import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def main() -> None:
    parser = default_parser("ann_runner")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    candidates = payload.get("ann_candidates", ["sparse_mlp", "gru", "ssm", "moe"])
    result = {
        "skill": "ann_runner",
        "run_id": args.run_id,
        "trained_ann_refs": {str(name): f"outputs/ann/{str(name)}.pt" for name in candidates},
        "training_summary": {"candidate_count": len(candidates), "status": "stub_completed"},
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
