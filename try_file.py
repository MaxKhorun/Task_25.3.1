from time import sleep
from settings import login_email, login_pass
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = 'https://petfriends.skillfactory.ru/'


def set_driver():
    """Создание и настройка драйвера для дальнейего использования в др. фикстурах и тестах"""
    options = webdriver.ChromeOptions()
    # options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    w_driver = webdriver.Chrome(options=options)
    w_driver.set_window_size(1200, 800)

    return w_driver


def log_in_func(set_driver):
    """Используя созданный драйвер из фикстуры выше, логинеимся на сайт и проверяем, что получилось войти.
    дальше можно уже работать с сайтом в авторизованном состоянии."""
    driver = set_driver
    driver.get(base_url + 'login')

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


def check(log_in_func):
    w_driver = log_in_func
    # amount_of_pets = int
    pets_header = w_driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    txt = pets_header.text
    w_driver.quit()

    txt = txt[txt.index('в')+1:txt.index('Д')]
    temp_numlist_from_txt = [i for i in txt if i.isdigit()]
    amountof_pets = int(''.join(temp_numlist_from_txt))

    """t = "M.Kh \
Питомцев: 109 \
Друзей: 0 \
Сообщений: 0 "


t = t[t.index('в') + 1:t.index('Д')]
numb_list = [i for i in t if i.isdigit()]
nums = int(''.join(numb_list))
print(t)
print(nums)"""

check(log_in_func(set_driver()))