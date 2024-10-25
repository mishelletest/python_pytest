from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Base class for all page objects"""

    def __init__(self, driver, timeout=10):
        """Initialize the base page with WebDriver and timeout."""
        self.driver = driver
        self.timeout = timeout

    def find_element(self, by, value):
        """Find a single web element."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"Element not found: {value}")
            return None

    def find_elements(self, by, value):
        """Find multiple web elements."""
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
            return elements
        except TimeoutException:
            print(f"Elements not found: {value}")
            return []

    def click_element(self, by, value):
        """Click on a web element."""
        element = self.find_element(by, value)
        if element:
            element.click()

    def enter_text(self, by, value, text):
        """Enter text into a web element (e.g., input field)."""
        element = self.find_element(by, value)
        if element:
            element.clear()
            element.send_keys(text)

    def get_element_text(self, by, value):
        """Get the text from a web element."""
        element = self.find_element(by, value)
        if element:
            return element.text
        return ""

    def is_element_visible(self, by, value):
        """Check if an element is visible on the page."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False

    def get_title(self):
        """Return the current page title."""
        return self.driver.title

    def get_url(self):
        """Return the current URL."""
        return self.driver.current_url

    def handle_alert(self) -> str:
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text