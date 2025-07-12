#!/bin/bash

# Check yt-dlp presence
if ! command -v yt-dlp &> /dev/null; then
    echo "yt-dlp is not installed. Install it first."
    exit 1
fi

# Validate URL input
if [ -z "$1" ]; then
    echo "Usage: $0 <YouTube-URL>"
    exit 1
fi

URL="$1"

# Get full subtitle list
SUB_LIST=$(yt-dlp --list-subs "$URL" 2>/dev/null)

# Filter: only 'en' and 'de' variants with at least one subtitle format
VALID_SUBS=$(echo "$SUB_LIST" | awk '
  /^[a-z]{2}(-[a-zA-Z]{2})?[[:space:]]/ {
    lang=$1;
    for (i=2; i<=NF; i++) {
      if ($i ~ /vtt|srv|ttml|json/) {
        if (lang ~ /^en(-|$)/ || lang ~ /^de(-|$)/) {
          print lang;
          break;
        }
      }
    }
  }
' | sort -u)

# Check if any valid subtitles exist
if [ -z "$VALID_SUBS" ]; then
    echo "No valid English or German subtitles available."
    exit 0
fi

# Display list
echo "Available subtitles:"
i=1
declare -A LANG_MAP
for lang in $VALID_SUBS; do
    echo "$i) $lang"
    LANG_MAP[$i]=$lang
    ((i++))
done

# Prompt user
read -rp "Choose subtitle language number to download: " CHOICE
SELECTED_LANG=${LANG_MAP[$CHOICE]}

if [ -z "$SELECTED_LANG" ]; then
    echo "Invalid selection."
    exit 1
fi

echo "Downloading subtitles for: $SELECTED_LANG"
yt-dlp --write-sub --sub-lang "$SELECTED_LANG" --skip-download --convert-subs srt "$URL"

echo "Done."

