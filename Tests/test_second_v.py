import time

from pages.auth_page import AuthPage
from settings import login_email, login_pass


def test_auth_page(driver):
    page = AuthPage(driver)
    page.email(login_email)
    page.password(login_pass)
    page.btn_click()

    assert page.get_relative_link() == '/my_pets'

    time.sleep(5)