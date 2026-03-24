import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def main() -> None:
    parser = default_parser("result_reporter")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    result = {
        "skill": "result_reporter",
        "run_id": args.run_id,
        "validation_report_ref": payload.get("validation_report_ref", "outputs/reports/validation_report.md"),
        "confidence_summary": payload.get("confidence_summary", {"default": "moderate"}),
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
