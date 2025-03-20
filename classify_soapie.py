import sys
import json
from transformers import pipeline

# Load pipeline untuk text classification
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Ambil teks dari argumen
text = sys.argv[1]

# Daftar kategori SOAPIE
soapie_labels = ["Subjective", "Objective", "Assessment", "Plan"]

# Klasifikasikan teks ke dalam kategori SOAPIE
result = classifier(text, candidate_labels=soapie_labels)

# Format hasil sebagai dictionary
soapie_categories = {label: score for label, score in zip(result["labels"], result["scores"])}

# Cetak hasil sebagai JSON agar bisa dibaca oleh PHP
print(json.dumps(soapie_categories))
