import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def main() -> None:
    parser = default_parser("task_prototype_library_builder")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    prototypes = payload.get("prototype_definitions", ["Proto-Memory", "Proto-Switch", "Proto-Local"])
    result = {
        "skill": "task_prototype_library_builder",
        "run_id": args.run_id,
        "prototype_library_ref": payload.get("prototype_library_ref", "data/prototypes/v1"),
        "prototype_pirg_refs": {name: f"data/prototypes/v1/pirg/{str(name).lower().replace('proto-', 'proto_')}.pirg" for name in prototypes},
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
