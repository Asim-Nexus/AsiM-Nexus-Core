import pyautogui, time, pyperclip

def asim_read_answer():
    print("[AsiM] CEO jyu, ma Gemini ko answer read gardai xu...")
    time.sleep(5) # जेमिनाइलाई उत्तर लेख्न समय दिने
    
    # १. स्क्रिनको बीचमा क्लिक गर्ने (Focus)
    pyautogui.click(x=500, y=500)
    
    # २. 'Ctrl+A' र 'Ctrl+C' गरेर सबै टेक्स्ट कपी गर्ने (सिम्पल तरिका)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    # ३. कपी भएको टेक्स्ट पढ्ने
    answer = pyperclip.paste()
    print("\n[AsiM] --- Read Success ---")
    print(answer[:500] + "...") # सुरुको केही भाग देखाउने
    print("\n[AsiM] Maile Gemini ko answer bujhe. Aba ma yeslai process garchu.")

if __name__ == "__main__":
    asim_read_answer()
