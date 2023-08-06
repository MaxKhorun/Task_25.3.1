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

    pets_header = w_driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    pets_header = pets_header.text
    pets_header = pets_header[pets_header.index('в')+1:pets_header.index('Д')]
    temp_numlist_from_txt = [i for i in pets_header if i.isdigit()]

    amount_of_pets = int(''.join(temp_numlist_from_txt))

    list_of_pets = w_driver.find_elements(By.CSS_SELECTOR, "tbody > tr > td") #selector to data line


    dict_with_pets = {
        'names': [list_of_pets[it].text for it in range(0, len(list_of_pets), 4)],
        'breed': [list_of_pets[it].text for it in range(1, len(list_of_pets), 4)],
        'age': [list_of_pets[it].text for it in range(2, len(list_of_pets), 4)]
                      }
    print(
        dict_with_pets['names'], '\n',
        dict_with_pets['breed'], '\n',
        dict_with_pets['age'], '\n',
          )

    print(set(dict_with_pets['names']), "\n",
          len(set(dict_with_pets['names'])))
    f = set(dict_with_pets['names'])
    print(f[0])

check_pets(log_in_func(set_driver()))

"""    pets_info = []
    for i in range(len(list_of_pets)):
        pet_info = list_of_pets[i].text

        name = pet_info.split("\n")[0]

        pets_info.append(name)
        # breed = pet_info.split("\n")[1]
        # pets_info.append(breed)
        # # age = pet_info.split("\n")[2]
        # # pets_info.append(age)

    print(pets_info)
    print(pets_info[0].split())"""