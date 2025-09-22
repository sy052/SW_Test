import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web.login import LoginPage

class TestLogin:

    def test_success_login(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("tomsmith", "SuperSecretPassword!")
 
        # 로그인 성공 시 나타나는 메시지를 기다렸다가 확인합니다.
        flash_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        message = flash_elem.text
        assert "You logged into a secure area!" in message, (
            f"예상된 성공 메시지가 표시되지 않았습니다. 받은 메시지: {message}"
        )

    @pytest.mark.parametrize("username, password", [
        ("wrong_user", "wrong_pass"),
        ("tomsmith", "wrong_pass"),
    ])
    def test_failed_login(self, driver, username, password):
        login = LoginPage(driver)
        login.open()
        login.login(username, password)
        assert not login.is_login_successful(), "예상치 못한 로그인 성공"
