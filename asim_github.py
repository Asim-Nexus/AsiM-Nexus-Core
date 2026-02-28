import webbrowser
import pyautogui
import time
def asim_join_github():
    print("[AsiM] CEO jyu, ma tapai ko GitHub account ma connect huna jandaixu...")
    # १. सिधै गिटहब खोल्ने
    webbrowser.open("https://github.com/asimnexus00")
    time.sleep(5) # पेज खुल्न समय दिने
    # २. 'Follow' वा 'Sign In' बटनमा जान माउस हल्लाउने (Visual confirmation)
    print("[AsiM] GitHub profile scan gardaixu. System integration active...")
    pyautogui.moveTo(500, 500, duration=1) 
    # ३. रिपोर्ट अपडेट गर्ने
    with open("C:\\AsiM_Nexus\\GitHub_Status.txt", "w") as f:
        f.write("AsiM is now attempting to link with GitHub: asimnexus00")
    print("[Success] GitHub link attempt complete. CEO jyu, login chaine bhaye login gardinu hos.")
if __name__ == "__main__":
    asim_join_github()
