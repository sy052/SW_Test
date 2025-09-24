
#tests/test_login.py

import pytest
from web.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture 
def driver():
    #웹 창 뜨는것 : 헤드리스트
    opts = Options()
    #백그라운드로 테스트 하는 옵션 추가
    # $env:HEADLESS="true"
    if os.getenv("HEADLESS","false").lower() == "true":
        opts.add_argument("--headless=new") 
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(opts) #크롬 드라이버 가져올 때 이 옵션을 가져옴
    yield driver
    driver.quit()

#autouse=True:모든 테스트 함수(파라미터 각 케이스 포함) 앞에서 자동 실행됩니다.
@pytest.fixture(autouse=True)  
def reset_state(driver):
    driver.delete_all_cookies() # 쿠키/스토리지 정리
    driver.get("about:blank")
    yield

LOGIN_CASES = [("tomsmith","SuperSecretPassword!", "You logged into a secure area!"),
               ("tom","SuperSecretPassword!", "Your username is invalid"),
               ("tomsmith","S","Your password is invalid!"),
               ("","","Your username is invalid")]

@pytest.mark.parametrize("username,pw,expected", LOGIN_CASES)
def test_login_cases(driver, username,pw,expected):  #driver를 fixture로 둠
    #driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.login(username,pw)
    msg = page.flash_message()
    print(f"flash msg : {page.flash_message()}")
    assert expected in msg
 