import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()   # You can parameterize this to use different browsers
    driver.maximize_window()
    driver.get("https://google.com")
    request.cls.driver = driver
    yield
    driver.quit()
