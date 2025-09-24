#tests/test_signup_mock.py

import json
import pytest
from playwright.sync_api import sync_playwright
from web.signup_pw import SignupPage  #url 가져옴

URL = "file:///D:\swtest\web\signup_mock.html" 

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

CASES = [
    {
        "id": "success",
        "status": 200,
        "json_body": {"status": "ok", "message": "회원가입 성공(Mocked)"}, #서버가 보낸 메세지 - 가짜
        "expected": "회원가입 성공(Mocked)", #expected는 TC. - 실제 확인
    },
    {
        "id": "fail",
        "status": 500,
        "json_body": {"status": "error", "message": "서버 오류(Mocked)"},
        "expected": "서버 오류(Mocked)", 
    },
]

@pytest.mark.parametrize("case", CASES) #playwright는 page.route 핸들러를 def handler(route, request) 형태로 호출
def test_signup_mock(page, case):
   
    def fake_signup_api(route, request): #테스트를 위해 가짜로 만듬
        route.fulfill( #채워주는 함수
            status=case["status"],
            content_type = "application/json",
            body=json.dumps(case['json_body']) #위 CASES안의 json_body
        )
    page.route("**/api/signup", fake_signup_api) #객체 생성할 때 page 넘겨줌

    signup = SignupPage(page)
    signup.open(URL)
    signup.fill_form("user@exa.com", "tester", "abcd12345", "abcd12345", True) #이메일,사용자명,비밀번호,비밀번호확인,약관동의
    signup.submit()
    flash = signup.flash_message()

    assert flash == case["expected"]
    #assert case["expected"] in flash #dict에 원하는 키 값이 있는지 확인, dict는 ['expected'].

