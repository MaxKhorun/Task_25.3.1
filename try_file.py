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


def check_pets(log_in_func):
    w_driver = log_in_func
    # amount_of_pets = int
    pets_header = w_driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    pets_header = pets_header.text
    pets_header = pets_header[pets_header.index('в')+1:pets_header.index('Д')]
    temp_numlist_from_txt = [i for i in pets_header if i.isdigit()]
    amount_of_pets = int(''.join(temp_numlist_from_txt))

    list_of_pets = w_driver.find_elements(By.CSS_SELECTOR, ".table>tbody>tr") #selector to name field
    # count_pets = list_of_pets

    # print(discr_list)
    print(amount_of_pets)
    # print(count_pets)
    w_driver.quit()
    # assert amount_of_pets == list_of_pets
    # return amount_of_pets
    assert 'friend' in w_driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>td')



check_pets(log_in_func(set_driver()))