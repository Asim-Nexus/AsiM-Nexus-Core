import threading
import time
import os
class AsiMAgent:
    def __init__(self, name, task_type):
        self.name = name
        self.task_type = task_type
        self.knowledge_base = []
    def work(self, task_detail):
        print(f"[{self.name}] Task सुरु गर्दैछु: {task_detail}")
        time.sleep(2) # काम गरिरहेको समय
        result = f"{self.name} ले '{task_detail}' सफलतापूर्वक सम्पन्न गर्‍यो।"
        self.knowledge_base.append(result)
        print(f"[{self.name}] Success: {result}")
        return result
def as_manager():
    # एजेन्टहरू निर्माण
    researcher = AsiMAgent("Researcher-Alpha", "Web Search")
    coder = AsiMAgent("Coder-Beta", "GitHub Automation")
    print("[AsiM Engine] Multi-Agent System Active भयो।")
    # एजेन्टहरूलाई एकैसाथ काममा लगाउने (Threading)
    t1 = threading.Thread(target=researcher.work, args=("Nepal's AI Future 2026 data collection",))
    t2 = threading.Thread(target=coder.work, args=("Updating GitHub with latest AI structures",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("[AsiM Engine] सबै एजेन्टहरूले आफ्नो 'Experience' शेयर गरे। असिमले नयाँ कुरा सिक्यो!")
if __name__ == "__main__":
    as_manager()
