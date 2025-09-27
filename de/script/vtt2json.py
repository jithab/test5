import re
import json
import sys
import os

def parse_timestamp(ts):
    """Convert WebVTT timestamp (hh:mm:ss.mmm or mm:ss.mmm) to seconds."""
    parts = ts.strip().split(':')

    if len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
    elif len(parts) == 2:
        hours = 0
        minutes = int(parts[0])
    else:
        raise ValueError(f"Invalid timestamp format: {ts}")

    secs_parts = parts[-1].split('.')
    if len(secs_parts) != 2:
        raise ValueError(f"Invalid seconds format in timestamp: {ts}")

    seconds = int(secs_parts[0])
    milliseconds = int(secs_parts[1])

    return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000

def read_vtt(file_path):
    entries = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if '-->' in line:
            start_ts, end_ts = [t.strip() for t in line.split('-->')]
            start_sec = parse_timestamp(start_ts)
            end_sec = parse_timestamp(end_ts)

            i += 1
            text_lines = []
            while i < len(lines) and lines[i].strip():
                text_lines.append(lines[i].strip())
                i += 1

            sentence = ' '.join(text_lines)
            entries.append({
                "start": round(start_sec, 3),
                "end": round(end_sec, 3),
                "de": sentence,
                "en": ""
            })
        else:
            i += 1

    return {
        "title": "<title>",
        "author": "© Deutsche Welle",
        "author_url": "<author url>",
        "lines": entries,
        "words": [{
            "de": "",
            "ipa": "",
            "en": ""
        }]
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_vtt.py <file.vtt>")
        sys.exit(1)

    vtt_path = sys.argv[1]

    if not os.path.isfile(vtt_path):
        print(f"Error: File '{vtt_path}' does not exist.")
        sys.exit(1)

    try:
        subtitles = read_vtt(vtt_path)
        json_path = os.path.splitext(vtt_path)[0] + '.json'
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(subtitles, f, indent=4, ensure_ascii=False)
        print(f"JSON written to {json_path}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
