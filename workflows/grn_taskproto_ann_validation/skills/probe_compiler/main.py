import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def main() -> None:
    parser = default_parser("probe_compiler")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    families = payload.get("probe_family_definitions", {})
    result = {
        "skill": "probe_compiler",
        "run_id": args.run_id,
        "compiled_probes": families,
        "mapping_summary": payload.get("condition_mapping_overrides", {}),
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
