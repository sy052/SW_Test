#web/login_pw.py

from playwright.sync_api import Page, sync_playwright
# from web.login_pw import LoginPage

class LoginPage: #include
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = "#username"
    PASSWORD = "#password"
    SUBMIT   = "button[type='submit']"
    FLASH    = "#flash"
   # EXPECTED = "You logged into a secure area!"

    
    def __init__(self, page: Page):
        self.page = page
        #self.url = URL

    def open(self):
        # 자동 대기: 페이지가 로드될 때까지 적절히 기다림
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        # 자동 대기: 요소가 표시/활성될 때까지 fill/click가 자체적으로 기다립니다.
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.SUBMIT)

    def flash_message(self) -> str:
        # locator는 표시/텍스트 가능 상태가 될 때까지 자동 대기
        msg = self.page.locator(self.FLASH).inner_text()
        return msg.strip()
