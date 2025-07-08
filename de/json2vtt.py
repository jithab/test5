import json
import sys

def seconds_to_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    milliseconds = int((secs - int(secs)) * 1000)
    return f"{hours:02}:{minutes:02}:{int(secs):02}.{milliseconds:03}"

def convert_json_to_vtt(json_filename):
    with open(json_filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("WEBVTT\n")
    for item in data.get("sents", []):
        start_ts = seconds_to_timestamp(item["start"])
        end_ts = seconds_to_timestamp(item["end"])
        print(f"{start_ts} --> {end_ts}")
        print(item["sent"])
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python json_to_vtt.py <input_file.json>", file=sys.stderr)
        sys.exit(1)

    convert_json_to_vtt(sys.argv[1])
