import pytest
from time import sleep
from settings import login_email, login_pass
from selenium import webdriver
from selenium.webdriver.common.by import By

fixt = pytest.fixture
base_url = 'https://petfriends.skillfactory.ru/'


@fixt
def set_driver():
    """Создание и настройка драйвера для дальнейего использования в др. фикстурах и тестах"""
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    w_driver = webdriver.Chrome(options=options)
    w_driver.set_window_size(1200, 800)

    return w_driver

@fixt
def log_in_func(set_driver):
    """Используя созданный драйвер из фикстуры выше, логинеимся на сайт и проверяем, что получилось войти.
    дальше можно уже работать с сайтом в авторизованном состоянии."""
    driver = set_driver
    driver.get(base_url+'login')

    email_fld = driver.find_element(By.CSS_SELECTOR, 'input#email')
    email_fld.clear()
    email_fld.send_keys(login_email)


    pass_fld = driver.find_element(By.CSS_SELECTOR, 'input#pass')
    pass_fld.clear()
    pass_fld.send_keys(login_pass)

    submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_btn.click()

    btn_to_mypets = driver.find_element(By.CSS_SELECTOR, "a[href='/my_pets']")
    btn_to_mypets.click()

    assert driver.current_url == f'{base_url}my_pets'
    return driver


