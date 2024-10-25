from selenium.webdriver.support.ui import Select

def select_by_value(driver, locator, value):
    dropdown = Select(driver.find_element(*locator))
    dropdown.select_by_value(value)

def select_by_visible_text(driver, locator, text):
    dropdown = Select(driver.find_element(*locator))
    dropdown.select_by_visible_text(text)

def select_by_index(driver, locator, index):
    dropdown = Select(driver.find_element(*locator))
    dropdown.select_by_index(index)
