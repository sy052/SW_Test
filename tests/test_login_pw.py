# test/test_login_pw.py

import pytest
from playwright.sync_api import sync_playwright
from web.login_pw import LoginPage #class 전체 가져옴

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


#page만 계속 새로 오픈됨
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

# 파라미터화
LOGIN_CASES = [("tomsmith","SuperSecretPassword!", "You logged into a secure area!"),
            ("tom","SuperSecretPassword!", "Your username is invalid"),
            ("tomsmith","S","Your password is invalid!"),
            ("","","Your username is invalid")]

@pytest.mark.parametrize("username,pw,expected", LOGIN_CASES)
#test 함수 안에 page 함수를 인자로 설정해줌.
def test_login_cases_pw(page, username, pw, expected):  #driver를 fixture로 둠
    page = LoginPage(page)
    page.open() #def open()
    page.login(username,pw) #def login()
    msg = page.flash_message() #def flash_message()
    print(f"\nflash msg : {msg}")
    
    assert expected in msg

    # msg = page.locator("#finish").inner_text().strip() # #:id name, strip(): 앞뒤로 공백 자름
    # assert EXPECTED in msg



