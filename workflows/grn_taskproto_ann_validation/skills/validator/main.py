import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def main() -> None:
    parser = default_parser("validator")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    policy = payload.get("validation_policy", {})
    result = {
        "skill": "validator",
        "run_id": args.run_id,
        "validation_metrics": {"policy": policy, "status": "stub_completed"},
        "failure_cases": payload.get("failure_cases", []),
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
