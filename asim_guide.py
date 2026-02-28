import os, webbrowser
def asim_guide():
    print("[AsiM] Opening Google Cloud Console for CEO...")
    print("[Guide] 1. Create Project 'AsiM-System'")
    print("[Guide] 2. Enable 'Gmail API'")
    print("[Guide] 3. Download credentials.json to C:\AsiM_Nexus")
    webbrowser.open("https://console.cloud.google.com/apis/library/gmail.googleapis.com")

if __name__ == "__main__":
    asim_guide()
