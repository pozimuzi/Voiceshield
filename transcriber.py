 
# This script converts Hindi audio to text using the Vosk model.

from vosk import Model, KaldiRecognizer
import wave
import json
import os

def clean_transcript(text):
    replacements = {
        "पकड़": "pakad",
        "चेक": "check",
        "अकाउंट": "account",
        "पैसा": "paise",
        "ओटीपी": "otp",
        "ओ टी पी": "otp",
        "टोटली": "totally",
        "फ्री गिफ्ट": "free gift",
        "बैंक": "bank",
        "अकौंट": "account"
    }
    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)
    return text

def transcribe_audio(audio_path):
    model_path = os.path.join(os.getcwd(), "models", "vosk-model-small-hi-0.22")
    if not os.path.exists(model_path):
        raise Exception(f" Model path not found: {model_path}")

    wf = wave.open(audio_path, "rb")
    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            results.append(result.get("text", ""))

    final_text = " ".join(results).strip()
    final_text = clean_transcript(final_text)
    print(" Cleaned transcript:", final_text)
    return final_text
