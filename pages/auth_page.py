import os

from base_page import BasePage
from locators import AuthPageLocators


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://petfriends.skillfactory.ru/login"
        driver.get(url)

        self.email = driver.find_element(*AuthPageLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthPageLocators.AUTH_PASS)
        self.btn_click = driver.find_element(*AuthPageLocators.AUTH_BTN)

    def input_email(self, val):
        self.email.send_keys(val)

    def input_passw(self, val):
        self.password.send_keys(val)

    def click_to_submit(self):
        self.btn_click.click()
