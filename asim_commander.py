import asyncio
from playwright.async_api import async_playwright
import time
async def asim_handle_software(task_url, instruction):
    print(f"[AsiM] CEO jyu, ma online software '{task_url}' handle gardaixu...")
    async with async_playwright() as p:
        # ब्राउजर खोल्ने (headless=False गर्दा तपाईँले असिमले काम गरेको देख्न सक्नुहुन्छ)
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        try:
            await page.goto(task_url)
            print(f"[AsiM] Page load bhayo. Instruction: {instruction}")
            # नमुनाको लागि: गुगलमा 'Multiverse Peace' सर्च गर्ने
            # तपाईँले यहाँ जुनसुकै सफ्टवेयरको बटन क्लिक गर्ने कमाण्ड लेख्न सक्नुहुन्छ
            if "google" in task_url:
                await page.fill('textarea[name="q"]', instruction)
                await page.keyboard.press("Enter")
                time.sleep(3)
                print("[Success] AsiM le software bhitra task pura garyo.")
            # काम सकिएपछि स्क्रिनशट लिने (प्रमाणको लागि)
            await page.screenshot(path="C:\\AsiM_Nexus\\AsiM_Task_Report.png")
        except Exception as e:
            print(f"[Error] Task garda samasya aayo: {e}")
        time.sleep(2)
        await browser.close()
        print("[AsiM] Browser closed. Mission Accomplished.")
if __name__ == "__main__":
    # यहाँ तपाईँले असिमलाई कुनै पनि URL र काम दिन सक्नुहुन्छ
    asyncio.run(asim_handle_software("https://www.google.com", "Nepal's position in Global AI Index 2026"))
