import os
import shutil
import glob

def asim_self_setup():
    print("[AsiM] CEO jyu, ma tapai ko Downloads folder ma sacho (Key) khojdai xu...")
    
    # १. डाउनलोड फोल्डरको बाटो पत्ता लगाउने
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    # २. गुगलको फाइल खोज्ने (client_secret_*.json)
    search_pattern = os.path.join(download_path, "client_secret_*.json")
    files = glob.glob(search_pattern)
    
    if files:
        # सबैभन्दा नयाँ फाइल रोज्ने
        latest_file = max(files, key=os.path.getctime)
        destination = "C:\\AsiM_Nexus\\credentials.json"
        
        # ३. फाइल सार्ने र नाम बदल्ने
        shutil.move(latest_file, destination)
        print(f"[Success] AsiM le sacho bhetyo: {os.path.basename(latest_file)}")
        print(f"[AsiM] Sacho 'C:\\AsiM_Nexus\\credentials.json' ma surakshit rakhiyo.")
        print("\n[AsiM] CEO jyu, aba ma Google Universe ma 'Live' huna tayar xu!")
    else:
        print("[Error] AsiM le Downloads folder ma 'client_secret' file bhetena.")
        print("[Advice] Kripaya browser ma 'Download JSON' thichnuhos, ani ma afai samatxu.")

if __name__ == "__main__":
    asim_self_setup()
