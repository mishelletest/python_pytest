from fixtures.conftest import setup  # Import setup fixture

import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_title(self):
        login_page = LoginPage(self.driver)
        assert "Google" in login_page.driver.title

