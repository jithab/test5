import json
import sys
import os

def merge_subtitle_lines(data):
    merged_lines = []
    i = 0
    while i < len(data["lines"]):
        current = data["lines"][i]
        if not current["de"].strip().endswith(('.', '!', '?')) and i + 1 < len(data["lines"]):
            next_line = data["lines"][i + 1]
            merged = {
                "start": current["start"],
                "end": next_line["end"],
                "en": f'{current["en"]} {next_line["en"]}',
                "de": f'{current["de"]} {next_line["de"]}'
            }
            merged_lines.append(merged)
            i += 2
        else:
            merged_lines.append(current)
            i += 1
    return {"lines": merged_lines}

def main():
    if len(sys.argv) != 2:
        print("Usage: python merge_subtitles.py <input_file.json>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    merged = merge_subtitle_lines(data)
    json.dump(merged, sys.stdout, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()

