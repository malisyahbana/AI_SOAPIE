<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['audio_file'])) {
    // Path file audio yang diterima
    $audioFile = $_FILES['audio_file']['tmp_name'];

    // 1. Konversi audio ke format PCM WAV (16kHz, mono) menggunakan ffmpeg
    $processedAudioFile = 'processed_audio.wav';
    $conversionCommand = "ffmpeg -i " . escapeshellarg($audioFile) . " -ar 16000 -ac 1 -c:a pcm_s16le " . escapeshellarg($processedAudioFile);
    shell_exec($conversionCommand);

    // 2. Jalankan Vosk untuk Speech-to-Text
    $voskOutput = shell_exec("python3 vosk_transcribe.py " . escapeshellarg($processedAudioFile));

    // 3. Jalankan Transformers untuk klasifikasi teks SOAPIE
    $soapieClassification = shell_exec("python3 classify_soapie.py " . escapeshellarg($voskOutput));

    // Kembalikan hasil dalam format JSON
    echo json_encode([
        'transcribed_text' => $voskOutput,
        'soapie_classification' => json_decode($soapieClassification),
        'form_data' => $_POST
    ]);
} else {
    echo json_encode(['error' => 'No audio file uploaded']);
}
?>
