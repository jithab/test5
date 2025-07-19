import json
import epitran

# Initialize Epitran for German
epi = epitran.Epitran('deu-Latn')

# Input and output file paths
input_file = 'input.json'
output_file = 'output_with_ipa.json'

# Read JSON data from file
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Process each entry
for entry in data.get("lines"):
    german_text = entry.get("de", "")
    ipa_transcription = epi.transliterate(german_text)
    entry["ipa"] = ipa_transcription

# Write updated data to output file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"IPA transcriptions written to '{output_file}'.")

