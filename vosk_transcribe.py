import sys
import wave
import numpy as np
from vosk import Model, KaldiRecognizer
import json

# Path ke model Vosk
model_path = "model"
model = Model(model_path)

# Ambil file audio
audio_file = sys.argv[1]
wf = wave.open(audio_file, "rb")

# Pastikan format audio sesuai
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Format audio tidak didukung. Harus WAV mono PCM16.")
    sys.exit(1)

recognizer = KaldiRecognizer(model, wf.getframerate())
recognizer.SetWords(True)

# Proses dan konversi suara ke teks
text = ""
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text += result.get("text", "") + " "

# Ambil teks akhir
final_result = json.loads(recognizer.FinalResult())
text += final_result.get("text", "")

print(text.strip())  # Kembalikan teks
