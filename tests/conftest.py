#250902 #tests/test_login.py 옮겨옴
# tests/conftest.py
import pytest
from apps.calculator import Calculator
from web.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

#픽스쳐(fixture)
#@pytest.fixture(scope="class") #테스트도 클래스 기반으로 만들어야 함 , 테스트 마다 실행
@pytest.fixture(scope="module")
def calculator_instance(): # calculator_instance() : decoration 함수 
    c = Calculator() # 반복되는 함수 지정한 후 변환
    print("\n계산기 인스턴스 생성")
    return c

@pytest.fixture(scope="session")
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

