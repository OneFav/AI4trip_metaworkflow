import argparse
import json
from pathlib import Path
from typing import Any


def read_json(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def write_json(path: str, payload: dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def default_parser(skill_name: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=skill_name)
    parser.add_argument("--input", dest="input_path", default=None)
    parser.add_argument("--output", dest="output_path", required=True)
    parser.add_argument("--run-id", dest="run_id", default="local_run")
    return parser
