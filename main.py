while True:
    audio = record_until_silence()    # wait for the person to finish a sentence
    text = transcribe(audio)          # stt.py
    english = translate(text)         # translate.py
    speak(english)                    # tts.py