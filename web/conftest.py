import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    opts = Options()
    opts.add_experimental_option("detach", True)
    opts.add_argument("--window-size=1280,900")
    #opts.add_argument("--headless=new")

    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()
