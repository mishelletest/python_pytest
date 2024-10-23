import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    """Fixture to initialize the browser and handle setup/teardown."""
    driver = webdriver.Chrome()  # You can replace with Firefox or another browser
    driver.maximize_window()

    # Yield the driver so it's available to the test
    yield driver

    # Quit the driver after the test completes
    driver.quit()
