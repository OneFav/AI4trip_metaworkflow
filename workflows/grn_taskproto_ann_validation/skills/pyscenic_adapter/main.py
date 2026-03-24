import importlib.util
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def has_pyscenic() -> bool:
    return importlib.util.find_spec("pyscenic") is not None


def main() -> None:
    parser = default_parser("pyscenic_adapter")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    available = has_pyscenic()
    result = {
        "skill": "pyscenic_adapter",
        "run_id": args.run_id,
        "regulon_activity_ref": "outputs/grn/regulon_activity.csv" if available else "outputs/grn/regulon_activity.stub.csv",
        "grn_adjacency_ref": "outputs/grn/grn_adjacency.tsv" if available else "outputs/grn/grn_adjacency.stub.tsv",
        "dependency": {"pyscenic_available": available},
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
