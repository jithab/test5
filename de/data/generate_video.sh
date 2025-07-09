#!/bin/bash

# Usage: ./generate_centered_subs_1080p.sh input.mp3 input.vtt output.mp4

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 input.mp3 input.vtt output.mp4"
  exit 1
fi

AUDIO="$1"
VTT="$2"
OUTPUT="$3"
ASS="styled_subs.ass"
BLACK_VIDEO="black_1080p.mp4"

# Check dependencies
command -v ffmpeg >/dev/null || { echo "❌ ffmpeg is required."; exit 1; }
command -v ffprobe >/dev/null || { echo "❌ ffprobe is required."; exit 1; }

# Step 1: Convert VTT to ASS
echo "🎯 Converting VTT to ASS..."
ffmpeg -i "$VTT" "$ASS"

# Step 2: Inject corrected style into the ASS file
echo "🎯 Updating subtitle style..."
STYLE_LINE='Style: Default,Arial,24,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,150,0,0,1,3,0,5,30,30,0,1'
sed -i "/^Style: Default/c\\$STYLE_LINE" "$ASS"

# Step 3: Get audio duration
echo "🎯 Getting audio duration..."
DURATION=$(ffprobe -i "$AUDIO" -show_entries format=duration -v quiet -of csv="p=0")

# Step 4: Create black 1080p video
echo "🎯 Creating 1920x1080 black video..."
ffmpeg -f lavfi -i color=c=black:s=1920x1080:r=30 -t "$DURATION" \
-c:v libx264 -pix_fmt yuv420p -preset veryfast "$BLACK_VIDEO"

# Step 5: Merge everything with subtitle rendering
echo "🎯 Generating final video..."
ffmpeg -i "$BLACK_VIDEO" -i "$AUDIO" -vf "ass=$ASS" \
-c:v libx264 -c:a aac -b:a 192k -shortest "$OUTPUT"

echo "✅ Done: '$OUTPUT' created at 1920x1080 with font size 32 and centered subtitles."
