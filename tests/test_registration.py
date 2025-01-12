import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.data import TestData
from helpers.locators import PageLocators
from helpers.methods import generate_random_email, generate_secure_password, registration_of_new_user, authorization_of_registered_user


class TestRegistration:

    def test_registration_success(self, driver):
        first_name = random.choice(TestData.FIRST_NAMES)
        user_email = generate_random_email(first_name)
        secure_password = generate_secure_password()

        # Вызов метода регистрации нового пользователя
        registration_of_new_user(driver, first_name, user_email, secure_password)

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER))
        )
        time.sleep(1)

        # Проверка URL-адреса на соответствие профилю внутри этого метода
        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, user_email, secure_password)


    def test_registration_incorrect_password(self, driver):
        first_name = random.choice(TestData.FIRST_NAMES)
        user_email = generate_random_email(first_name)

        # Вызов метода регистрации нового пользователя с вводом некорректного пароля
        registration_of_new_user(driver, first_name, user_email, "000")

        # Проверка сообщения об ошибке "Некорректный пароль"
        assert driver.find_element(By.XPATH, PageLocators.TEXT_INCORRECT_PASSWORD).text == "Некорректный пароль"
