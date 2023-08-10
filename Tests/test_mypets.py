import pytest
from selenium.webdriver.common.by import By


def test_verify_quantity(log_in_func):
    w_driver = log_in_func
    w_driver.implicitly_wait(10)
    pets_header = w_driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left').text
    # withdrowing text from webelement in one line
    pets_header = pets_header[pets_header.index('в') + 1:pets_header.index('Д')]
    # cutting both side by indexes of items. We know it, so we can afford it now
    amount_of_pets = int(''.join(i for i in pets_header if i.isdigit()))
    # getting integer value from text by int-func over ''.join-ing the string line which we got from list generator with condition: if ?.isdigit()
    list_of_pets = w_driver.find_elements(By.CSS_SELECTOR, "tbody>tr")
    # looking for array of pets on web-page

    assert amount_of_pets == len(list_of_pets)


# @pytest.mark.xfail(reason='AssertionError')
def test_all_pets_object(log_in_func):
    driver = log_in_func
    driver.implicitly_wait(10)
    all_images = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>th>img')
        # Получили информацию о картинках в карточках животных
    list_of_pets = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
        # получили список строк с данными питомцев.
    descriptions = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>td')
        # получили все данные о животных списком: в списке будут имена, породы, возраст.

    pets_info = {
        'names': [descriptions[it].text for it in range(0, len(descriptions), 4)],
        'breed': [descriptions[it].text for it in range(1, len(descriptions), 4)],
        'age': [descriptions[it].text for it in range(2, len(descriptions), 4)]
    }
    comparison_list = [[pets_info['names'][i], pets_info['breed'][i], pets_info['age'][i]]
                       for i in range(len(list_of_pets))]
        # Лист для поиска идентичных животных

    count_images = [True for i in all_images if i.get_attribute('src') != '']
        # counting pets with images in cards. Assembling to the list as True value.

    for it in range(len(list_of_pets)):
        assert pets_info['names'][it] != ''  # 3
        assert pets_info['breed'][it] != ''  # 3
        assert pets_info['age'][it] != ''  # 3
        assert comparison_list[it] != comparison_list[(it + 1) % len(list_of_pets)] #проверка дублей
        assert all_images[it].get_attribute('src') != ''

    assert len(pets_info['names']) == len(set(pets_info['names']))  # 2

    assert len(count_images) > len(list_of_pets) / 2  # 1
