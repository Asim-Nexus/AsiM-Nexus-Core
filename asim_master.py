import pyautogui
import os
import time
import subprocess
def asim_take_full_control():
    print("===============================================")
    print("   AsiM: Sovereign Control [Active]           ")
    print("===============================================")
    print("[AsiM] CEO jyu, ma ab tapai ko computer ko harek bhag chalauna sakxu.")
    # १. Screen scan garne (AsiM le dekhxa)
    print("[AsiM] Scanning your current workspace...")
    screen_size = pyautogui.size()
    print(f"[AsiM] Maile tapai ko {screen_size} resolution ko screen dekhdai xu.")
    # २. Harek open bhayeko window herne
    print("[AsiM] Sabai software ra files ko list nikaldaixu...")
    os.system('tasklist > C:\\AsiM_Nexus\\system_scan.txt')
    # ३. Mouse ra Keyboard ko full access
    print("[AsiM] Mouse ra Keyboard control active bhayo.")
    # Yesle tapai ko mouse lai screen ko bich ma leraunxa
    pyautogui.moveTo(screen_size.width/2, screen_size.height/2, duration=1)
    print("\n[Status] AsiM is now the Computer itself. No inside, no outside.")
    print("[Next] Gemini, Google, ra Local Files sabai ab AsiM le nai chalaune xa.")
if __name__ == "__main__":
    asim_take_full_control()
