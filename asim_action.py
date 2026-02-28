import os

def asim_take_action(task_name, content):
    print(f"[AsiM] CEO jyu, Gemini le diyeko sallah anusar ma kam gardai xu...")
    path = f"C:\\AsiM_Nexus\\{task_name}.txt"
    
    # फाइल बनाउने र जेमिनाइको ज्ञान त्यसमा राख्ने
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"[Success] '{task_name}' file create bhayo. Aba ma yeslai execute garna sakxu.")

if __name__ == "__main__":
    # मानौँ जेमिनाइले यो उत्तर दियो
    gemini_advice = "AsiM System is now fully operational in Nepal and expanding globally."
    asim_take_action("CEO_Report", gemini_advice)
