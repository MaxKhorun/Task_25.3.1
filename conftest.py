import time
from datetime import datetime

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from settings import login_email, login_pass
from selenium import webdriver
from selenium.webdriver.common.by import By

fixt = pytest.fixture
base_url = 'https://petfriends.skillfactory.ru/'



# @fixt(params=["Chrome", "Firefox"], scope="class")
@fixt
def set_driver():

    """Создание и настройка драйвера для дальнейего использования в др. фикстурах и тестах"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    w_driver = webdriver.Chrome(options=options)
    w_driver.set_window_size(1200, 800)
    """
    if request.param == "Chrome":
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        w_driver = webdriver.Chrome(options=options)
        w_driver.set_window_size(1200, 800)
    if request.param == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        w_driver = webdriver.Firefox(options=options)"""

    return w_driver

@fixt
def log_in_func(set_driver):
    """Используя созданный драйвер из фикстуры выше, логинеимся на сайт и проверяем, что получилось войти.
    дальше можно уже работать с сайтом в авторизованном состоянии."""
    driver = set_driver
    driver.get(base_url+'login')

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email'))).clear()
    driver.find_element(By.ID, 'email').send_keys(login_email)
    # driver.find_element(By.ID, 'email').send_keys(login_email)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'pass'))).clear()
    # driver.find_element(By.ID, 'pass').send_keys(login_email)
    # driver.find_element(By.ID, 'pass').clear()
    driver.find_element(By.ID, 'pass').send_keys(login_pass)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/my_pets']")))
    driver.find_element(By.CSS_SELECTOR, "a[href='/my_pets']").click()

    assert driver.current_url == f'{base_url}my_pets'

    yield driver

    driver.quit()



