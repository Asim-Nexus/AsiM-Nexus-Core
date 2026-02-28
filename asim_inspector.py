import subprocess
import os
def asim_inspect_code():
    repo = "Asim-Nexus/AsiM-Nexus-Core"
    print(f"[AsiM] CEO jyu, ma '{repo}' bhitra ko code ko DNA herdai xu...")
    # १. रिपो भित्रका फाइलहरूको लिस्ट हेर्ने
    result = subprocess.run(['gh', 'repo', 'view', repo, '--json', 'files'], capture_output=True, text=True)
    if result.returncode == 0:
        import json
        files_data = json.loads(result.stdout)
        files_list = [f['path'] for f in files_data.get('files', [])]
        print(f"[Success] Maile {len(files_list)} wota file bhetaye.")
        # २. एउटा विस्तृत रिपोर्ट बनाउने
        analysis_path = "C:\\AsiM_Nexus\\AsiM_Code_DNA.txt"
        with open(analysis_path, "w", encoding="utf-8") as f:
            f.write(f"========== AsiM GitHub Code Analysis ==========\n")
            f.write(f"Repository: {repo}\n")
            f.write(f"Scan Time: {os.popen('date /t').read().strip()}\n\n")
            f.write("Files Found in the Heart of AsiM:\n")
            for file in files_list:
                f.write(f"- {file}\n")
        print(f"[AsiM] Sabai file ko list '{analysis_path}' ma save bhayo.")
        print("\n--- Files in your Repo ---")
        for file in files_list:
            print(f"📄 {file}")
    else:
        print("[AsiM] CEO jyu, code padna sakiyena. Repo ma file nahuna sakxa ki?")
if __name__ == "__main__":
    asim_inspect_code()
