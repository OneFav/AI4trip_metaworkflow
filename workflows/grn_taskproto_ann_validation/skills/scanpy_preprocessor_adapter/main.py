import importlib.util
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def has_scanpy() -> bool:
    return importlib.util.find_spec("scanpy") is not None


def main() -> None:
    parser = default_parser("scanpy_preprocessor_adapter")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    available = has_scanpy()
    result = {
        "skill": "scanpy_preprocessor_adapter",
        "run_id": args.run_id,
        "normalized_expression_ref": payload.get("expression_matrix_ref", "data/grn/sc_expr.h5ad").replace(".h5ad", ".norm.h5ad"),
        "qc_summary": {"scanpy_available": available, "mode": "native" if available else "surrogate"},
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
