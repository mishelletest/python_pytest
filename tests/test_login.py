from fixtures.conftest import setup  # Import setup fixture
import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_title(self):
        login_page = LoginPage(self.driver)
        assert "Login Page" in login_page.driver.title

    def test_admin_login(self):
        login_page = LoginPage(self.driver)
        login_page.user_login()
        alert_message = login_page.handle_alert()
        assert alert_message == "Login successful.", f"Alert message mismatch: {alert_message}"


