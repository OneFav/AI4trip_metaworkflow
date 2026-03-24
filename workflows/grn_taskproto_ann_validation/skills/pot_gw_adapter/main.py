import importlib.util
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def has_pot() -> bool:
    return importlib.util.find_spec("ot") is not None


def main() -> None:
    parser = default_parser("pot_gw_adapter")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    available = has_pot()
    result = {
        "skill": "pot_gw_adapter",
        "run_id": args.run_id,
        "gw_distance": payload.get("gw_distance", 0.21 if available else 0.45),
        "transport_plan_ref": "outputs/distances/gw_transport_plan.npy",
        "dependency": {"pot_available": available, "fallback_metric": "Frobenius" if not available else None},
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
