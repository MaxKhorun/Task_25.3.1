import pytest
from selenium.webdriver.common.by import By

from conftest import base_url


def test_verify_quantity(log_in_func):
    w_driver = log_in_func
    pets_header = w_driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left').text
            # withdrowing text from webelement in one line
    pets_header = pets_header[pets_header.index('в') + 1:pets_header.index('Д')]
            #cutting both side by indexes of items. We know it, so we can afford it now
    amount_of_pets = int(''.join(i for i in pets_header if i.isdigit()))
            #getting integer value from text by int-func over ''.join-ing the string line which we got from list generator with condition: if ?.isdigit()
    list_of_pets = w_driver.find_elements(By.CSS_SELECTOR, "tbody>tr")
            #looking for array of pets on web-page
    w_driver.quit()
    assert amount_of_pets == len(list_of_pets)

def test_all_pets_object():
    pass


# def test_mypets_correct_amount(log_in_func):
#     w_driver = log_in_func
#     amount_of_pets = int
#     pets_header = w_driver.find_element(By.TAG_NAME, 'h2')
#     for el in pets_header:
#         print(el.text)
#
#     amounts_of_cards = int
#     """запросить значение с поля _Питомцы_, запросить кол-во карточек ->n сравнить цифры. создать своё исключение, возможно"""
#     w_driver.find_element(By.XPATH, "//h1[contains(text(), 'PetFriends')]")
#     assert w_driver.current_url == f'{base_url}my_pets'


"""Проверка, что у пвины питомцев есть фотографии"""

def check_all_photos():
    pass

"""Проверить, что у всехз питомцев есть данные в полях: _имя_, _возраст_, _порода_"""

"""У всех питомцев разные имена"""

"""В списке нет повторяющихся питомцев"""