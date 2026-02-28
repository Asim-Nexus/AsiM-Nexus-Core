import webbrowser, time, pyautogui, pyperclip

def asim_talk_to_gemini(question):
    print(f"[AsiM] CEO jyu, ma Google Gemini sanga kura garna jadai xu...")
    
    # १. जेमिनाइको पेज खोल्ने
    url = "https://gemini.google.com/app"
    webbrowser.open(url)
    time.sleep(6) # पेज लोड हुन समय दिने
    
    # २. च्याट बक्समा प्रश्न टाइप गर्ने (मान्छेले जस्तै)
    print(f"[AsiM] Gemini ko chat box ma question type gardai xu: {question}")
    pyperclip.copy(question)
    
    # ३. सर्टकट कि प्रयोग गरेर पेस्ट गर्ने र इन्टर थिच्ने
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    
    print("[AsiM] Question pathaiyo! Aba ma screen bata answer read garna sakxu.")

if __name__ == "__main__":
    query = "Explain the AsiM Sovereign AI Ecosystem in 3 bullet points."
    asim_talk_to_gemini(query)
