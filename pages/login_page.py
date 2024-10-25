from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.dropdown import *

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="button"]')

    def enter_username(self, username: str):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def user_login(self, username: str ='admin', password: str ='admin', login: bool =True):
        self.enter_username(username)
        self.enter_password(password)
        dropdown_locator = ('id', 'role')
        select_by_value(self.driver, dropdown_locator, 'Admin')
        if login:
            self.click_login()