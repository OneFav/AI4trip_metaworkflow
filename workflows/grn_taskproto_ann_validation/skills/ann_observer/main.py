import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def main() -> None:
    parser = default_parser("ann_observer")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    candidates = payload.get("ann_candidates", [])
    result = {
        "skill": "ann_observer",
        "run_id": args.run_id,
        "ann_response_matrices": [
            {"ann": str(name), "matrix_ref": f"outputs/response/ann_{str(name)}_matrix.npy"}
            for name in candidates
        ],
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
