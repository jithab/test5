#!/bin/bash

# Check if filename was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <audio_file>"
  exit 1
fi

# Input audio file
audio_file="$1"

# Extract base name without extension
base_name="$(basename "$audio_file" | sed 's/\.[^.]*$//')"

# Run whisper with specified options
whisper "$audio_file" \
  --language German \
  --task transcribe \
  --output_format vtt 

