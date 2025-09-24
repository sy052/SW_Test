#web/plw_basic.py
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com/")
        print( page.title() )
        page.screenshot(path="screenshot.png")

def mrun():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page1 = browser.new_page()
        page1.goto("https://www.google.com/")
        print( page1.title() )

        page2 = browser.new_page()
        page2.goto("https://www.naver.com/")
        print( page2.title() )

        #input() #자동으로 페이지 닫히는거 막기 위함. 터미널에서 엔터해야 닫힘.

if __name__ == "__main__" :
    #run()
    mrun()
