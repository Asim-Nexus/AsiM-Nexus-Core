import webbrowser

def asim_ask_gemini(question):
    print(f"[AsiM] CEO jyu, ma tapai ko question liyera Google Gemini ma jadai xu...")
    print(f"[AsiM] Question: {question}")
    # Gemini को URL मा सिधै प्रश्न पठाउने (Browser Mode)
    url = f"https://gemini.google.com/app"
    webbrowser.open(url)
    print("[AsiM] Browser khulyo. Aba ma tya manxe le jastai process garna sakxu.")

if __name__ == "__main__":
    query = "Asim AI ecosystem kasari chalaune?"
    asim_ask_gemini(query)
