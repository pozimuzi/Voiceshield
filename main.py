from transcriber import transcribe_audio
from classifier import is_scam
from alert_ui import show_result_window

audio_file = "sample_audio/scam1.wav"

print(" Transcribing audio...")
try:
    transcript = transcribe_audio(audio_file)
    print("\n Transcript:\n", transcript)

    print("\n Checking for scam keywords...")
    scam, found_keywords = is_scam(transcript)

    result_data = {"is_scam": scam, "suspicious": found_keywords}

    if scam:
        print("Result: Likely SCAM call!")
        print("Keywords Detected:", ", ".join(found_keywords))
    elif found_keywords:
        print(" Suspicious: Some scam keywords found.")
    else:
        print(" Result: Call looks safe.")

    show_result_window(transcript, result_data)

except Exception as e:
    print(" Error:", str(e))
