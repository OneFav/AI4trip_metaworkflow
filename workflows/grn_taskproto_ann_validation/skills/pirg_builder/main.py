import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def main() -> None:
    parser = default_parser("pirg_builder")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    matrices = payload.get("response_matrices", payload.get("grn_response_matrices", []))
    result = {
        "skill": "pirg_builder",
        "run_id": args.run_id,
        "pirg_refs": [
            {"id": item.get("id", f"obj_{idx+1}"), "pirg_ref": f"outputs/pirg/{item.get('id', f'obj_{idx+1}')}.pirg"}
            for idx, item in enumerate(matrices)
            if isinstance(item, dict)
        ],
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
