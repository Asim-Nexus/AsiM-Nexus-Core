import webbrowser, os, time, shutil

def asim_auto_work():
    print("[AsiM] CEO jyu, ma aafai credentials nikaalna jadai xu...")
    # १. सिधै Credentials बनाउने ठाउँ खोल्ने
    url = "https://console.cloud.google.com/apis/credentials/oauthclient"
    webbrowser.open(url)
    
    print("[AsiM] Please click 'Create' in the browser. I am waiting for the file...")
    
    # २. डाउनलोड फोल्डर कुरेर बस्ने (६० सेकेन्ड सम्म)
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    found = False
    for i in range(60):
        for file in os.listdir(download_path):
            if file.startswith("client_secret_") and file.endswith(".json"):
                src = os.path.join(download_path, file)
                dst = "C:\\AsiM_Nexus\\credentials.json"
                shutil.move(src, dst)
                print(f"[Success] AsiM le 'credentials.json' aafai setup garyo!")
                found = True
                break
        if found: break
        time.sleep(1)
    
    if not found:
        print("[Alert] AsiM le file भेटेन। कृपया 'Download JSON' थिच्नुहोस्।")

if __name__ == "__main__":
    asim_auto_work()
