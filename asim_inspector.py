import subprocess
import os
import json
def asim_deep_scan():
    repo = "Asim-Nexus/AsiM-Nexus-Core"
    print(f"[AsiM] CEO jyu, ma '{repo}' bhitra ko real-time DNA check gardaixu...")
    # सिधै गिटहबको फाइल लिस्ट तान्ने (force refresh)
    cmd = f"gh api repos/{repo}/contents?ref=main"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        files_data = json.loads(result.stdout)
        print(f"[Success] AsiM le antat: {len(files_data)} wota objects bhetayo!")
        print("\n--- 🧬 AsiM Core DNA (Files Found) ---")
        for item in files_data:
            icon = "📁" if item['type'] == 'dir' else "📄"
            print(f"{icon} {item['name']}")
        # एउटा नयाँ कन्फर्मेसन फाइल बनाउने
        with open("C:\\AsiM_Nexus\\AsiM_Final_DNA.txt", "w", encoding="utf-8") as f:
            f.write(f"AsiM Sovereign Core: Online\nVerified Files: {len(files_data)}")
    else:
        print("[AsiM] CEO jyu, API le ajhai error diyo. Kripaya 10 second parkhinu hos.")
if __name__ == "__main__":
    asim_deep_scan()
