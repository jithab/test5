import webvtt
import json
import re
import sys
import os

def time_to_seconds(timestamp):
    """Convert VTT timestamp (hh:mm:ss.mmm) to float seconds."""
    hours, minutes, rest = timestamp.split(":")
    seconds, milliseconds = rest.split(".")
    return round(int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000, 3)

def clean_text(text):
    """Remove newlines, trim spaces, and collapse multiple spaces."""
    text = text.replace('\n', ' ')
    text = text.strip()
    text = re.sub(r'\s{2,}', ' ', text)
    return text

def combine_vtt_to_json(en_path, de_path):
    # Read English subtitles
    en_map = {
        (cap.start, cap.end): clean_text(cap.text)
        for cap in webvtt.read(en_path)
    }

    # Read German subtitles
    de_map = {
        (cap.start, cap.end): clean_text(cap.text)
        for cap in webvtt.read(de_path)
    }

    # Find matching timestamp pairs
    common_keys = sorted(set(en_map.keys()) & set(de_map.keys()))

    if not common_keys:
        raise ValueError("No matching subtitle timestamps found.")

    lines = []
    for start, end in common_keys:
        lines.append({
            "start": time_to_seconds(start),
            "end": time_to_seconds(end),
            "en": en_map[(start, end)],
            "de": de_map[(start, end)]
        })

    # Print JSON to stdout
    print(json.dumps({"lines": lines}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python combine_vtt_subtitles.py <english.vtt> <german.vtt>")
        sys.exit(1)

    en_file = sys.argv[1]
    de_file = sys.argv[2]

    if not os.path.exists(en_file) or not os.path.exists(de_file):
        print("❌ Error: One or both VTT files do not exist.")
        sys.exit(1)

    combine_vtt_to_json(en_file, de_file)

