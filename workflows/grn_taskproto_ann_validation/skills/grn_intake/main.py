import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def main() -> None:
    parser = default_parser("grn_intake")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    grn_items = payload.get("grn_items", [])
    result = {
        "skill": "grn_intake",
        "run_id": args.run_id,
        "normalized_grn_refs": [
            {"id": item.get("id", f"grn_{idx+1}"), "normalized_ref": item.get("source", "")}
            for idx, item in enumerate(grn_items)
            if isinstance(item, dict)
        ],
        "observation_summary": {
            "level": payload.get("grn_observation_level", "module"),
            "count": len(grn_items),
        },
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
