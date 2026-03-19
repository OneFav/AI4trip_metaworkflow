import sys
import json
import argparse
import traceback

def parse_challenge(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Basic parsing logic to separate the model and the human challenge
        parts = content.split("## 2. Human Challenge")
        if len(parts) < 2:
            return {"error": "Invalid format. Cannot find '## 2. Human Challenge' section."}
            
        model_part = parts[0].replace("## 1. Chosen Mathematical Model", "").strip()
        challenge_part = parts[1].strip()
        
        return {
            "status": "success",
            "model_context": model_part,
            "human_challenge": challenge_part
        }
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}

def main():
    parser = argparse.ArgumentParser(description="Parse Human Challenge for Stage 3")
    parser.add_argument("--input", required=True, help="Path to stage_3_input.md")
    parser.add_argument("--output", required=True, help="Path to save the parsed JSON")
    
    args = parser.parse_args()
    
    result = parse_challenge(args.input)
    
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        
    if "error" in result:
        print(f"Error parsing challenge: {result['error']}")
        sys.exit(1)
    else:
        print(f"Successfully parsed challenge. Wrote to {args.output}")

if __name__ == "__main__":
    main()
