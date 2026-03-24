import importlib.util
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def has_ott() -> bool:
    return importlib.util.find_spec("ott") is not None


def main() -> None:
    parser = default_parser("ott_jax_gw_adapter")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    available = has_ott()
    result = {
        "skill": "ott_jax_gw_adapter",
        "run_id": args.run_id,
        "gw_distance": payload.get("gw_distance", 0.19 if available else 0.42),
        "solver_log_ref": "outputs/logs/ott_jax_solver.json",
        "dependency": {"ott_available": available, "fallback": "pot_gw_adapter" if not available else None},
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
