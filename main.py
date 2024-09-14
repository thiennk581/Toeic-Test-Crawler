from playwright.async_api import async_playwright
import asyncio
from bs4 import BeautifulSoup
from json import dump
import os
from Crawler import *
from Test import *

fileJson = "test15.json"
folder = "ToeicTests"
os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, fileJson)

url = "https://estudyme.com/study/test/toeic-testpro/test-15-new-64a2947d1064127d35e7b87b/" #link test

parts = [f"Part {i}" for i in range(1,8)]



async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # browser = await p.chromium.launch(headless= False, slow_mo=100)
        page = await browser.new_page()
        await page.goto(url)
        await page.get_by_text('Start Now').click();
        await page.get_by_text('Nộp bài').click()
        await page.click("//button[text() = 'Submit']")

        questionsTest = [[]]
        for part in parts:
            await page.locator("#question-segment-palette-header-scroll-container").get_by_text(part).click()
            await page.is_visible('main-game-object')           #class
            await page.wait_for_timeout(3000)                   # waiting for loading all data
            html = await page.inner_html('#main-study-view')    #id

            soup = BeautifulSoup(html, 'html.parser')
            questions = soup.find_all('div', class_ = 'game-object-view-aio')

            questionsPart = []
            if (part == "Part 1"):
                questionsPart = [Crawler.questionInfoPart1(question)  for question in questions]
            elif (part == "Part 2"):
                questionsPart = [Crawler.questionInfoPart2(question)  for question in questions]
            elif (part == "Part 3"):
                questionsPart = [Crawler.questionClusterInfoPart34(Crawler,question)  for question in questions]
            elif (part == "Part 4"):
                questionsPart = [Crawler.questionClusterInfoPart34(Crawler, question)  for question in questions]
            elif (part == "Part 5"):
                questionsPart = [Crawler.questionInfoPart5(Crawler, question)  for question in questions]
            elif (part == "Part 6"):
                questionsPart = [Crawler.questionClusterInfoPart67(Crawler, question)  for question in questions]
            elif (part == "Part 7"):
                questionsPart = [Crawler.questionClusterInfoPart67(Crawler, question)  for question in questions]
            questionsTest.append(questionsPart)
            print(part, len(questionsPart))

        fullTest = Test(questionsTest= questionsTest).to_dict()     # dinh dang dict de ghi vao json
        with open(file_path, 'w') as file:
            dump(fullTest, file, indent=4)
        print(len(questionsTest))
        await browser.close()
        
        
asyncio.run(main())