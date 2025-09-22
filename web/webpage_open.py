
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opts = Options()
opts.add_experimental_option("detach", True)
#opts.add_argument("--headless=new")
opts.add_argument("--window-size=1280,900")

driver = webdriver.Chrome(options=opts)
try : 
    driver.get("https://www.python.org/")
    print(f"제목:{driver.title}")
    el = driver.find_element(By.NAME, 'q')
    el.clear()
    el.send_keys("pycon", Keys.RETURN)

finally:
    pass
    #driver.quit()