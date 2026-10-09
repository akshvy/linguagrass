import ollama

def translate(text, src="Hindi", tgt="English"):
    r = ollama.chat(model="qwen2.5:3b", messages=[
        {"role": "system", "content": f"You are a live interpreter. Translate {src} to {tgt}. Keep idioms natural. Output only the translation."},
        {"role": "user", "content": text},
    ])
    return r["message"]["content"].strip()

if __name__ == "__main__":
    print(translate("भाई, यहाँ से स्टेशन कितनी दूर है?"))