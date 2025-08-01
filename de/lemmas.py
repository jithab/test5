import json
import sys
import stanza


# Load input JSON file from first command-line argument
if len(sys.argv) < 2:
    print("Usage: python script.py input.json")
    sys.exit(1)

# Initialize Stanza
stanza.download('de')  # Only needed once
nlp = stanza.Pipeline('de', processors='tokenize,pos,lemma', use_gpu=False)

input_path = sys.argv[1]

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract all "de" sentences
sentences = [line['de'] for line in data.get("lines", []) if "de" in line]

# Collect unique verb lemmas
lemmas = dict()


mytype = {
    "NOUN": "n",
    "VERB": "v",
    "ADJ": "adj",
    "ADV": "adv"
}

for sentence in sentences:
    doc = nlp(sentence)
    for sent in doc.sentences:
        for word in sent.words:
            if word.upos in ["NOUN", "VERB", "ADJ", "ADV"]:
                lemmas[word.lemma]=mytype[word.upos]

# Prepare output JSON array
output = [
    {"de": de, "ipa": "", "en": "", "ps": ps}
    for de, ps in sorted(lemmas.items(), key=lambda x: x[0].lower())
]

# Print output JSON
print(json.dumps(output, ensure_ascii=False, indent=2))

