description: "解析 Stage 3 中人类提出的质疑反例，以便后续进行模型调整。"

---

# challenge_response_parser

This skill reads the human challenge from the `stage_3_input.md` file and parses it into a structured format for the Agent to process.

## Usage

```bash
python main.py --input <path_to_stage_3_input.md> --output <path_to_parsed_json>
```

## Inputs
- `input`: Path to the markdown file containing the mathematical model and the human's edge-case challenges.

## Outputs
- A JSON file containing the extracted model context and the specific challenge scenarios.