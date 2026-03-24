import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def main() -> None:
    parser = default_parser("grn_observer")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    refs = payload.get("normalized_grn_refs", [])
    result = {
        "skill": "grn_observer",
        "run_id": args.run_id,
        "grn_response_matrices": [
            {"id": item.get("id", "grn_unknown"), "matrix_ref": f"outputs/response/{item.get('id', 'grn_unknown')}_matrix.npy"}
            for item in refs
            if isinstance(item, dict)
        ],
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
