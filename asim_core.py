import os, pickle, socket, webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Gmail र Drive को पूर्ण पहुँच (Full Control)
SCOPES = ['https://www.googleapis.com/auth/gmail.modify', 'https://www.googleapis.com/auth/drive']

def asim_init():
    os.system('cls')
    print("===============================================")
    print("   AsiM_Engine: Core V8 [Google Sovereign]    ")
    print(f"   CEO: Recognized | Identity: asimnexus00@gmail.com")
    print("   Capability: Full Account Management Active  ")
    print("===============================================")

def google_auth():
    creds = None
    token_path = 'C:\\AsiM_Nexus\\token.pickle'
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # यहाँ credentials.json चाहिन्छ (तपाईंले गुगलबाट डाउनलोड गरेको)
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
    return creds

def read_emails():
    creds = google_auth()
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=5).execute()
    messages = results.get('messages', [])
    
    print(f"\n[AsiM] Checking asimnexus00@gmail.com inboxes...")
    if not messages:
        print("No new emails found.")
    else:
        for msg in messages:
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()
            print(f"- Subject: {txt['snippet'][:50]}...")

if __name__ == "__main__":
    asim_init()
    print("Commands: 'login' | 'check_mail' | 'clone <url>' | 'exit'")
    while True:
        try:
            raw = input("\nAsiM_Admin> ").lower().split(maxsplit=1)
            if not raw: continue
            cmd = raw[0]
            arg = raw[1] if len(raw) > 1 else ""

            if cmd == 'login': google_auth(); print("[AsiM] Login successful.")
            elif cmd == 'check_mail': read_emails()
            elif cmd == 'exit': break
            else: print("AsiM: Order pending for asimnexus00 ecosystem.")
        except Exception as e: print(f"[Error] {e}")
