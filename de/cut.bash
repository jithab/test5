#!/bin/bash

# --- Validate arguments ---
if [[ $# -ne 3 ]]; then
  echo "Usage: $0 <input_mp3_file> <start_cut_seconds> <end_cut_seconds>"
  echo "Example: $0 song.mp3 10.5 5.2"
  exit 1
fi

input_file="$1"
cut_start="$2"
cut_end="$3"

# Check if input file exists
if [[ ! -f "$input_file" ]]; then
  echo "Error: File '$input_file' not found."
  exit 1
fi

# Get total duration using ffprobe
duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$input_file")

# Calculate trimmed duration = total - cut_start - cut_end
trimmed_duration=$(awk "BEGIN { result = $duration - $cut_start - $cut_end; print result }")

# Check for invalid duration
if awk "BEGIN { exit ($trimmed_duration <= 0) ? 0 : 1 }"; then
  echo "Error: Trimmed duration is zero or negative. Check your cut times."
  exit 1
fi

# Generate output filename with prefix
input_basename=$(basename "$input_file")
output_file="output_${input_basename}"

# Run ffmpeg: trim audio, remove metadata/art, copy audio
ffmpeg -i "$input_file" -ss "$cut_start" -t "$trimmed_duration" -map_metadata -1 -vn -c copy "$output_file"

echo "✅ Done! Output saved as: $output_file"

