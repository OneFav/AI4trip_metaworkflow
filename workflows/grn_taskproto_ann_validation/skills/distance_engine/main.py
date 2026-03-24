import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def main() -> None:
    parser = default_parser("distance_engine")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    metric = payload.get("distance_metric", "GW")
    grn_refs = payload.get("grn_pirg_refs", {})
    prototype_refs = payload.get("prototype_pirg_refs", {})
    result = {
        "skill": "distance_engine",
        "run_id": args.run_id,
        "distance_matrices": {"metric": metric, "grn_count": len(grn_refs), "prototype_count": len(prototype_refs)},
        "ranking_summary": {"status": "stub_completed", "metric": metric},
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
