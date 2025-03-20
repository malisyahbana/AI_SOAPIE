import sys
import json
from transformers import pipeline

# Load pipeline untuk klasifikasi teks
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Ambil teks transkripsi dari argumen
input_json = sys.argv[1]
data = json.loads(input_json)
text = data["text"]

# Daftar kategori SOAPIE
soapie_labels = ["Subjective", "Objective", "Assessment", "Plan", "Instruksi", "Evaluasi"]

# Klasifikasikan teks
result = classifier(text, candidate_labels=soapie_labels)

# Format hasil sebagai dictionary
soapie_categories = {label: score for label, score in zip(result["labels"], result["scores"])}

# Cetak hasil sebagai JSON agar bisa dibaca oleh PHP
print(json.dumps(soapie_categories))
