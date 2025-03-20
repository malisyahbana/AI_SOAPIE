import os

# Gantilah dengan path ke file kredensial yang benar
os.environ["b5f305ea4bf61bba62456e460d37b7167e588100"] = "ardent-gearbox-454302-p2-b5f305ea4bf6.json"

# Periksa apakah kredensial sudah diatur
if "b5f305ea4bf61bba62456e460d37b7167e588100" in os.environ:
    print("✅ Kredensial ditemukan:", os.environ["b5f305ea4bf61bba62456e460d37b7167e588100"])
else:
    print("❌ Kredensial belum dikonfigurasi.")
