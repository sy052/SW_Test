#web/test_login.py

import pytest
import time
import selenium
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    #웹페이지 로그인 코드
    def __init__(self, driver): #클래스 자체가 driver갖고 있음.
        self.driver = driver
        print(f"사이트:{driver.title}, __name__")
        pass

    def open(self):
        self.driver.get(self.URL)
        time.sleep(1)
        pass

    def login(self, username, password):
        username = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')
        btn = self.driver.find_element(By.CLASS_NAME, 'radius')

        username.clear()
        username.send_keys("tomsmith", Keys.COMMAND)
        password.clear()
        password.send_keys("SuperSecretPassword!", Keys.COMMAND)
        time.sleep(1)
        btn.click()
        time.sleep(1)
        pass

    def is_login_successful(self):
        return "Secure Area" in self.driver.title  # 로그인 성공 시 타이틀 확인 가능
    
    if __name__ == "__main__" :
        print("현재 파일 실행 중..")
