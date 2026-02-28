import asyncio
from playwright.async_api import async_playwright
import os
import time
async def asim_download_key():
    async with async_playwright() as p:
        print("[AsiM] CEO jyu, ma browser bhitrai xirera 'Download JSON' button thichdai xu...")
        # ब्राउजर खोल्ने (तपाईँले देख्ने गरी - Headless=False)
        browser = await p.chromium.launch(headless=False) 
        context = await browser.new_context()
        page = await context.new_page()
        # १. गुगल क्रेडिन्सियल पेजमा जाने
        await page.goto("https://console.cloud.google.com/apis/credentials")
        print("[AsiM] Page khulyo. Kripaya login xaina bhane login garnuhos...")
        # २. 'Desktop client 1' को डाउनलोड आइकन खोज्ने र क्लिक गर्ने
        # नोट: यो बटनको नाम वा आइकन 'Download' टेक्स्ट भएको ठाउँमा हुन्छ
        try:
            # डाउनलोड आइकन (icon-button) खोज्ने प्रयास
            await page.wait_for_selector('button[aria-label*="Download"]', timeout=30000)
            await page.click('button[aria-label*="Download"]')
            print("[AsiM] Download icon click bhayo!")
            # ३. 'DOWNLOAD JSON' बटन थिच्ने
            await page.wait_for_selector('text="DOWNLOAD JSON"', timeout=10000)
            async with page.expect_download() as download_info:
                await page.click('text="DOWNLOAD JSON"')
            download = await download_info.value
            # ४. फाइललाई सिधै C:\AsiM_Nexus\credentials.json मा राख्ने
            path = "C:\\AsiM_Nexus\\credentials.json"
            await download.save_as(path)
            print(f"[Success] AsiM le sacho (Key) thutera '{path}' ma rakhiyo!")
        except Exception as e:
            print(f"[AsiM] CEO jyu, maile button bhettina. Kripaya euta 'Click' gardinu hos, baaki ma garchu.")
        await browser.close()
if __name__ == "__main__":
    asyncio.run(asim_download_key())
