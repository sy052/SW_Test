# test/test_dynamic_loading.py

import pytest
from playwright.sync_api import sync_playwright

URL = "https://the-internet.herokuapp.com/dynamic_loading/2"
EXPECTED = "Hello World!"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_dynamic_loading_pw(page):
    page.goto(URL)
    page.click("#start button") # #:id name, button:button

    msg = page.locator("#finish").inner_text().strip() # #:id name, strip(): 앞뒤로 공백 자름

    assert EXPECTED in msg
#############################################################
# selenium
#############################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading_se(driver):
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    finish = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish")) #(): 튜플형태
    )
    #finish = driver.find_element(By.ID, "finish") #로딩시간을 안기다리므로 test 불가.
    assert EXPECTED in finish.text.strip() #앞뒤 공백 잘라라