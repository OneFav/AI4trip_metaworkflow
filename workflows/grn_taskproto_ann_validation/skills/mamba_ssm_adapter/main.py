import importlib.util
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from _common.skill_runtime import default_parser, read_json, write_json


def has_mamba() -> bool:
    return importlib.util.find_spec("mamba_ssm") is not None


def main() -> None:
    parser = default_parser("mamba_ssm_adapter")
    args = parser.parse_args()
    payload = read_json(args.input_path)
    available = has_mamba()
    result = {
        "skill": "mamba_ssm_adapter",
        "run_id": args.run_id,
        "mamba_checkpoint_ref": "outputs/ann/mamba_checkpoint.pt" if available else None,
        "ann_pirg_ref": "outputs/pirg/ann_mamba.pirg" if available else None,
        "training_metrics_ref": "outputs/ann/mamba_metrics.json" if available else None,
        "dependency": {"mamba_ssm_available": available},
    }
    write_json(args.output_path, result)


if __name__ == "__main__":
    main()
