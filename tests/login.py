import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import PageLocators
from helpers.methods import authorization_of_registered_user, user_email_for_login, secure_password_for_login


class TestLogin:

    def test_login_through_enter_account_button(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )
        time.sleep(1)

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, user_email_for_login, secure_password_for_login)

    def test_login_through_personal_account_button(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_P_PERSONAL_ACCOUNT))
        )
        time.sleep(1)

        # Поиск кнопки "Личный Кабинет" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_P_PERSONAL_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, user_email_for_login, secure_password_for_login)

    def test_login_through_register_page(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )
        time.sleep(1)

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.LINK_REGISTER))
        )
        time.sleep(1)

        # Поиск кнопки "Зарегистрироваться" и клик по ней
        driver.find_element(By.XPATH, PageLocators.LINK_REGISTER).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_REGISTER))
        )
        time.sleep(1)

        # Поиск кнопки "Войти" и клик по ней
        driver.find_element(By.XPATH, PageLocators.LINK_ENTER).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, user_email_for_login, secure_password_for_login)

    def test_login_through_password_recovery_page(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )
        time.sleep(1)

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.LINK_RECOVER_PASSWORD))
        )
        time.sleep(1)

        # Поиск кнопки "Восстановить пароль" и клик по ней
        driver.find_element(By.XPATH, PageLocators.LINK_RECOVER_PASSWORD).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.LINK_ENTER))
        )
        time.sleep(1)

        # Поиск кнопки "Войти" и клик по ней
        driver.find_element(By.XPATH, PageLocators.LINK_ENTER).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, user_email_for_login, secure_password_for_login)
