import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import PageLocators
from helpers.methods import authorization_of_registered_user, user_email_for_login, secure_password_for_login


class TestPassage:

    def test_passage_to_constructor(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )
        time.sleep(1)

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, user_email_for_login, secure_password_for_login)

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR))
        )
        time.sleep(1)

        # Поиск кнопки "Конструктор" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ORDER))
        )
        time.sleep(1)

        # Проверка URL-адреса на соответствие домашней страницы
        assert driver.current_url == PageLocators.BASE_URL + PageLocators.ROUTES["homepage"]

    def test_passage_to_logo(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )
        time.sleep(1)

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, user_email_for_login, secure_password_for_login)

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_LOGO))
        )
        time.sleep(1)

        # Поиск лого и клик по нему
        driver.find_element(By.XPATH, PageLocators.BUTTON_LOGO).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ORDER))
        )
        time.sleep(1)

        # Проверка URL-адреса на соответствие домашней страницы
        assert driver.current_url == PageLocators.BASE_URL + PageLocators.ROUTES["homepage"]

    def test_passage_to_personal_account(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_P_PERSONAL_ACCOUNT))
        )
        time.sleep(1)

        # Поиск кнопки "Личный Кабинет" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_P_PERSONAL_ACCOUNT).click()

        # Проверка URL-адреса на соответствие профилю внутри этого метода
        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, user_email_for_login, secure_password_for_login)

    def test_passage_to_sections(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )
        time.sleep(1)

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, user_email_for_login, secure_password_for_login)

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR))
        )
        time.sleep(1)

        # Поиск кнопки "Конструктор" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.SECTION_SAUCES))
        )
        time.sleep(1)

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" not in driver.find_element(By.XPATH, PageLocators.SECTION_SAUCES).get_attribute("class")
        time.sleep(1)

        # Поиск раздела "Соусы" и клик по ней
        driver.find_element(By.XPATH, PageLocators.SECTION_SAUCES).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.SECTION_SAUCES))
        )
        time.sleep(1)

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" in driver.find_element(By.XPATH, PageLocators.SECTION_SAUCES).get_attribute("class")
        time.sleep(1)

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" not in driver.find_element(By.XPATH, PageLocators.SECTION_BUNS).get_attribute("class")
        time.sleep(1)

        # Поиск раздела "Соусы" и клик по ней
        driver.find_element(By.XPATH, PageLocators.SECTION_BUNS).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.SECTION_BUNS))
        )
        time.sleep(1)

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" in driver.find_element(By.XPATH, PageLocators.SECTION_BUNS).get_attribute("class")
        time.sleep(1)

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" not in driver.find_element(By.XPATH, PageLocators.SECTION_FILLING).get_attribute("class")
        time.sleep(1)

        # Поиск раздела "Соусы" и клик по ней
        driver.find_element(By.XPATH, PageLocators.SECTION_FILLING).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.SECTION_FILLING))
        )
        time.sleep(1)

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" in driver.find_element(By.XPATH, PageLocators.SECTION_FILLING).get_attribute("class")
        time.sleep(1)