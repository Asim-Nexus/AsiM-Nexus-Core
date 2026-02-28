import subprocess
import time
import os
def asim_auto_sync():
    print("[AsiM] CEO jyu, ma 'Auto-Sync' mode ma chirdaixu...")
    print("[Status] Ma harek minute changes check garne xu.")
    try:
        while True:
            # १. केही नयाँ फाइल वा परिवर्तन छ कि चेक गर्ने
            status = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
            if status.stdout.strip():
                print(f"[AsiM] Changes detected! Syncing with GitHub...")
                subprocess.run(['git', 'add', '.'])
                subprocess.run(['git', 'commit', '-m', f"AsiM Auto-Evolution: {time.ctime()}"])
                subprocess.run(['git', 'push', 'origin', 'main'])
                print("[Success] GitHub updated automatically.")
            else:
                # केही परिवर्तन नभए चुपचाप बस्ने
                pass
            time.sleep(60) # १ मिनेटको ग्यापमा चेक गर्ने
    except KeyboardInterrupt:
        print("[AsiM] Auto-Sync paused. CEO jyu, ma standby ma xu.")
if __name__ == "__main__":
    asim_auto_sync()
