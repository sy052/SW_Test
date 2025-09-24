#2580902
# web / loginpage.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #locator 지정
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    # 웹페이지 로그인 코드 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        user = self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        user.clear()
        user.send_keys(username)

        pw = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
        pw.clear()
        pw.send_keys(password)

        submit_btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT))
        submit_btn.click()

    def flash_message(self):
        msg = self.wait.until(EC.visibility_of_element_located(self.FLASH)).text
        return msg.strip() # strip: 앞뒤 공백이 있다면 다 잘라라    

if __name__ == "__main__" :
    #loginpage class  동작 코드 작성
    driver = webdriver.Chrome()
    try:
        page = LoginPage(driver)
        page.open
        page.login("tomsmith","SuperSecretPassword!")
        print(f"flash msg : {page.flash_message()}")
    finally:
        driver.quit()
        #print("현재 파일 실행 중..")