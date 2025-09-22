#web/melon.py

import time
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
    driver.get("https://www.melon.com/")
    print(f"사이트:{driver.title}")
    el = driver.find_element(By.ID, 'top_search')
    el.clear()
    el.send_keys("BTS", Keys.RETURN)

    driver.find_element(By.CSS_SELECTOR, '[title="앨범 - 페이지 이동"]').click()
    time.sleep(1)
    #driver.find_element(By.CSS_SELECTOR, '[title="LOVE YOURSELF 結 'Answer' - 페이지 이동"]') .click() -> title안에 ''가 있으므로 불가. 
    driver.find_element(By.CSS_SELECTOR, '#frm > div > ul > li:nth-child(1) > div > a.thumb').click() #copy css selector
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '[title="Euphoria 곡정보"]').click()
    time.sleep(1)
    #driver.find_element(By.CLASS_NAME, 'lyric on')
    lyric = driver.find_element(By.ID, 'd_video_summary').text #ID안에 있는 text파일을 가지고 옴
    title = driver.find_element(By.CLASS_NAME, 'song_name').text

    print(f"제목: {title}")
    print(f"가사: {lyric}")

    with open(title+"2.txt", "w", encoding="utf-8") as f:
        f.write(lyric)
    print(f"{title}2.txt 파일에 가사가 저장되었습니다.")
finally:
    pass
    #driver.quit()