#web/login.py

import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://the-internet.herokuapp.com/login"

opts = Options()
opts.add_experimental_option("detach", True)
#opts.add_argument("--headless=new")
opts.add_argument("--window-size=1280,900")

driver = webdriver.Chrome(options=opts)
try: 
    driver.get(url)
    print(f"사이트:{driver.title}")
    el1 = driver.find_element(By.ID, 'username')
    el1.clear()
    el1.send_keys("tomsmith", Keys.COMMAND)

    el2 = driver.find_element(By.ID, 'password')
    el2.clear()
    el2.send_keys("SuperSecretPassword!", Keys.COMMAND)
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, 'radius').click()
    time.sleep(1)

finally:
    
    pass