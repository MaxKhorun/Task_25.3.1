from selenium.webdriver.common.by import By


class AuthPageLocators:
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, "pass")
    AUTH_BTN = (By.CLASS_NAME, "btn-success")


class SuccessLoginPageLocators:
    PF_main_page_btn = (By.LINK_TEXT, "PetFriends")  # link
    MY_PETS_btn = (By.LINK_TEXT, "/my_pets")  # link
    ALL_PETS_btn = (By.LINK_TEXT, "/all_pets")  # link
    LOG_OUT_tbn = (By.CLASS_NAME, "btn-outline-secondary")
