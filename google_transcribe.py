import sys
import json
import os
import wave
from google.cloud import speech

# Pastikan Google Cloud Credential sudah dikonfigurasi
os.environ["b5f305ea4bf61bba62456e460d37b7167e588100"] = "ardent-gearbox-454302-p2-b5f305ea4bf6.json"

# Ambil file audio dari argumen
audio_file = sys.argv[1]

# Konversi audio ke format Google Speech-to-Text (WAV PCM16, 16kHz, mono)
wf = wave.open(audio_file, "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Format audio tidak didukung. Harus WAV mono PCM16.")
    sys.exit(1)

# Inisialisasi klien Google Speech-to-Text
client = speech.SpeechClient()

# Baca file audio
with open(audio_file, "rb") as f:
    audio_data = f.read()

# Konfigurasi permintaan transkripsi
audio = speech.RecognitionAudio(content=audio_data)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="id-ID"
)

# Kirim permintaan transkripsi
response = client.recognize(config=config, audio=audio)

# Ambil hasil transkripsi
transcribed_text = " ".join([result.alternatives[0].transcript for result in response.results])

# Cetak hasil agar bisa dibaca oleh PHP
print(json.dumps({"text": transcribed_text}))
