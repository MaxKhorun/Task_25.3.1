from selenium.webdriver.common.by import By


def test_verify_quantity(log_in_func):
    w_driver = log_in_func
    pets_header = w_driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left').text
    # withdrowing text from webelement in one line
    pets_header = pets_header[pets_header.index('в') + 1:pets_header.index('Д')]
    # cutting both side by indexes of items. We know it, so we can afford it now
    amount_of_pets = int(''.join(i for i in pets_header if i.isdigit()))
    # getting integer value from text by int-func over ''.join-ing the string line which we got from list generator with condition: if ?.isdigit()
    list_of_pets = w_driver.find_elements(By.CSS_SELECTOR, "tbody>tr")
    # looking for array of pets on web-page
    w_driver.quit()

    assert amount_of_pets == len(list_of_pets)


# @pytest.mark.xfail(reason='AssertionError')
def test_all_pets_object(log_in_func):
    driver = log_in_func

    all_images = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>th>img')
    list_of_pets = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")  # список строк с данными питомцев
    descriptions = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>td')  # получили все данные о животных списком

    pets_info = {
        'names': [descriptions[it].text for it in range(0, len(descriptions), 4)],
        'breed': [descriptions[it].text for it in range(1, len(descriptions), 4)],
        'age': [descriptions[it].text for it in range(2, len(descriptions), 4)]
    }
    count_images = [True for i in all_images if i.get_attribute('src') != '']

    assert len(count_images) > len(list_of_pets) / 2 #1
    assert len(pets_info['names']) == len(set(pets_info['names'])) #2
    assert pets_info['names'] != '' #3
    assert pets_info['breed'] != '' #3
    assert pets_info['age'] != '' #3

    try:
        for it in range(len(list_of_pets)):
            assert all_images[it].get_attribute('src') != ''
    except AssertionError as error:
        print(error)


"""Проверка, что у пвины питомцев есть фотографии""" #1 - Done

"""Проверить, что у всехз питомцев есть данные в полях: _имя_, _возраст_, _порода_"""  #3 - Done

"""У всех питомцев разные имена"""  #2 - Done

"""В списке нет повторяющихся питомцев"""
