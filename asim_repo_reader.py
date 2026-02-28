import subprocess
import os
def asim_direct_scan():
    user = "Asim-Nexus"
    print(f"[AsiM] CEO jyu, ma सिधै '{user}' को Public Repositories स्क्यान गर्दैछु...")
    # सिधै गिट कमाण्ड प्रयोग गरेर रिपो लिस्ट गर्ने प्रयास
    try:
        # यो कमाण्डले सिधै गिटहबको रिमोट चेक गर्छ
        cmd = f"gh repo list {user} --limit 100"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            content = result.stdout
            print("[Success] Maile tapai ko repo haru bhetai hale!")
            report_path = "C:\\AsiM_Nexus\\Repo_Analysis_Report.txt"
            with open(report_path, "w", encoding="utf-8") as f:
                f.write(f"========== AsiM Repo List: {user} ==========\n\n")
                f.write(content)
            print(f"[AsiM] Report ready xa: {report_path}")
            print("\n--- Repo List Snapshot ---")
            print(content[:500] + "...") # अलिकति विवरण स्क्रिनमा देखाउने
        else:
            print("[AsiM] CEO jyu, 'gh' le ajhai error diyo. Aba ma browser batai scan garchu.")
            # यदि CLI ले काम गरेन भने ब्राउजरबाट डेटा तान्ने मोड
            import webbrowser
            webbrowser.open(f"https://github.com/{user}?tab=repositories")
    except Exception as e:
        print(f"[Error] {str(e)}")
if __name__ == "__main__":
    asim_direct_scan()
