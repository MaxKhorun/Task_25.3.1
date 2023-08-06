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

def test_all_pets_object(log_in_func):

    driver = log_in_func

    all_images = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>th>img') #получили все картинки
    descriptions = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>td') #получили все данные о животных списком

    pets_info = {
        'names': [descriptions[it].text for it in range(0, len(descriptions), 4)],
        'breed': [descriptions[it].text for it in range(1, len(descriptions), 4)],
        'age': [descriptions[it].text for it in range(2, len(descriptions), 4)]
    }

    for it in range(len(descriptions)):

        assert all_images[it].get_attribute('src') != ''
        assert (all_images[it].get_attribute('src') == bool) > len(pets_info['names'])
        assert len(pets_info['names']) == len(set(pets_info['names']))
        assert pets_info['names'] != ''
        assert pets_info['breed'] != ''
        assert pets_info['age'] != ''




"""Проверка, что у пвины питомцев есть фотографии"""

"""Проверить, что у всехз питомцев есть данные в полях: _имя_, _возраст_, _порода_"""

"""У всех питомцев разные имена"""

"""В списке нет повторяющихся питомцев"""