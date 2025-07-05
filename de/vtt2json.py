import re
import json
import sys
import os

def parse_timestamp(ts):
    """Convert WebVTT timestamp (hh:mm:ss.mmm) to seconds."""
    parts = ts.strip().split(':')
    if len(parts) != 3:
        raise ValueError(f"Invalid timestamp format: {ts}")
    
    hours = int(parts[0])
    minutes = int(parts[1])
    secs_parts = parts[2].split('.')
    seconds = int(secs_parts[0])
    milliseconds = int(secs_parts[1]) if len(secs_parts) > 1 else 0

    return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000

def read_vtt(file_path):
    entries = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Check for timestamp line
        if '-->' in line:
            start_ts, end_ts = [t.strip() for t in line.split('-->')]
            start_sec = parse_timestamp(start_ts)
            end_sec = parse_timestamp(end_ts)

            # Collect subtitle text
            i += 1
            text_lines = []
            while i < len(lines) and lines[i].strip():
                text_lines.append(lines[i].strip())
                i += 1

            sentence = ' '.join(text_lines)
            entries.append({
                "start": round(start_sec, 3),
                "end": round(end_sec, 3),
                "sent": sentence,
                "tran": "",
                "words": [
                    {
                        "w": "",
                        "m": "",
                        "e": ""
                    }
                ]
            })
        else:
            i += 1

    return entries

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_vtt.py <file.vtt>")
        sys.exit(1)

    vtt_path = sys.argv[1]

    if not os.path.isfile(vtt_path):
        print(f"Error: File '{vtt_path}' does not exist.")
        sys.exit(1)

    subtitles = read_vtt(vtt_path)
    print(json.dumps(subtitles, indent=4, ensure_ascii=False))

