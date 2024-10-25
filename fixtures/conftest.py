import os

import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()   # You can parameterize this to use different browsers
    driver.maximize_window()
    driver.get("http://localhost:8000/test_page_with_images.html")
    # file_path = os.path.abspath("/Users/mishelleiturriaga/Desktop/python/python_pytest/resources/testing_website/test_page_with_images.html")
    # driver.get("file://" + file_path)
    request.cls.driver = driver
    yield
    driver.quit()
