import pytest
from selenium.webdriver.common.by import By

from conftest import base_url


def test_mypets_correct_amount(log_in_func):
    w_driver = log_in_func
    amount_of_pets = int
    amounts_of_cards = int
    """запросить значение с поля _Питомцы_, запросить кол-во карточек ->n сравнить цифры. создать своё исключение, возможно"""
    w_driver.find_element(By.XPATH, "//h1[contains(text(), 'PetFriends')]")
    assert w_driver.current_url == f'{base_url}my_pets'

"""Проверка, что у пвины питомцев есть фотографии"""

def check_all_photos():
    pass

"""Проверить, что у всехз питомцев есть данные в полях: _имя_, _возраст_, _порода_"""

"""У всех питомцев разные имена"""

"""В списке нет повторяющихся питомцев"""