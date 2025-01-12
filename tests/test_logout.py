import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.data import TestData
from helpers.locators import PageLocators
from helpers.methods import authorization_of_registered_user


class TestLogout:

    def test_logout(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )
        time.sleep(1)

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, TestData.USER_EMAIL_FOR_LOGIN, TestData.SECURE_PASSWORD_FOR_LOGIN)

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_QUIT))
        )
        time.sleep(1)

        # Поиск кнопки "Выход" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_QUIT).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER))
        )
        time.sleep(1)

        # Проверка URL-адреса на соответствие логина
        assert driver.current_url == TestData.BASE_URL + TestData.ROUTES["login"]