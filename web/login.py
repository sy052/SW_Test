import time
import warnings
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(1)  # 필요시 명시적 대기 추가

    def login(self, username, password):
        el_user = self.driver.find_element(By.ID, "username")
        el_pass = self.driver.find_element(By.ID, "password")
        btn = self.driver.find_element(By.CLASS_NAME, "radius")

        el_user.clear()
        el_user.send_keys(username, Keys.COMMAND)
        el_pass.clear()
        el_pass.send_keys(password, Keys.COMMAND)
        time.sleep(1)
        btn.click()
        time.sleep(1)

    def is_login_successful(self):
        return "Secure Area" in self.driver.title  # 로그인 성공 시 타이틀 확인 가능
