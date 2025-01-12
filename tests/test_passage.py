from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.data import TestData
from helpers.locators import PageLocators
from helpers.methods import authorization_of_registered_user


class TestPassage:

    def test_passage_to_constructor(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, TestData.USER_EMAIL_FOR_LOGIN, TestData.SECURE_PASSWORD_FOR_LOGIN)

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR))
        )

        # Поиск кнопки "Конструктор" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ORDER))
        )

        # Проверка URL-адреса на соответствие домашней страницы
        assert driver.current_url == TestData.BASE_URL + TestData.ROUTES["homepage"]

    def test_passage_to_logo(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, TestData.USER_EMAIL_FOR_LOGIN, TestData.SECURE_PASSWORD_FOR_LOGIN)

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_LOGO))
        )

        # Поиск лого и клик по нему
        driver.find_element(By.XPATH, PageLocators.BUTTON_LOGO).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ORDER))
        )

        # Проверка URL-адреса на соответствие домашней страницы
        assert driver.current_url == TestData.BASE_URL + TestData.ROUTES["homepage"]

    def test_passage_to_personal_account(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_P_PERSONAL_ACCOUNT))
        )

        # Поиск кнопки "Личный Кабинет" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_P_PERSONAL_ACCOUNT).click()

        # Проверка URL-адреса на соответствие профилю внутри этого метода
        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, TestData.USER_EMAIL_FOR_LOGIN, TestData.SECURE_PASSWORD_FOR_LOGIN)

    def test_passage_to_section_buns(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, TestData.USER_EMAIL_FOR_LOGIN, TestData.SECURE_PASSWORD_FOR_LOGIN)

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR))
        )

        # Поиск кнопки "Конструктор" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.SECTION_SAUCES))
        )

        # Поиск раздела "Соусы" и клик по ней
        driver.find_element(By.XPATH, PageLocators.SECTION_SAUCES).click()

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" in driver.find_element(By.XPATH, PageLocators.SECTION_SAUCES).get_attribute("class")

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" not in driver.find_element(By.XPATH, PageLocators.SECTION_BUNS).get_attribute("class")

        # Поиск раздела "Соусы" и клик по ней
        driver.find_element(By.XPATH, PageLocators.SECTION_BUNS).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.SECTION_BUNS))
        )

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" in driver.find_element(By.XPATH, PageLocators.SECTION_BUNS).get_attribute("class")

    def test_passage_to_section_sauces(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, TestData.USER_EMAIL_FOR_LOGIN, TestData.SECURE_PASSWORD_FOR_LOGIN)

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR))
        )

        # Поиск кнопки "Конструктор" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.SECTION_SAUCES))
        )

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" not in driver.find_element(By.XPATH, PageLocators.SECTION_SAUCES).get_attribute("class")

        # Поиск раздела "Соусы" и клик по ней
        driver.find_element(By.XPATH, PageLocators.SECTION_SAUCES).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.SECTION_SAUCES))
        )

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" in driver.find_element(By.XPATH, PageLocators.SECTION_SAUCES).get_attribute("class")

    def test_passage_to_section_filling(self, driver):
        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT))
        )

        # Поиск кнопки "Войти в аккаунт" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER_ACCOUNT).click()

        # Вызов метода для проверки успешной авторизации
        authorization_of_registered_user(driver, TestData.USER_EMAIL_FOR_LOGIN, TestData.SECURE_PASSWORD_FOR_LOGIN)

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR))
        )

        # Поиск кнопки "Конструктор" и клик по ней
        driver.find_element(By.XPATH, PageLocators.BUTTON_P_CONSTRUCTOR).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.SECTION_FILLING))
        )

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" not in driver.find_element(By.XPATH, PageLocators.SECTION_FILLING).get_attribute("class")

        # Поиск раздела "Соусы" и клик по ней
        driver.find_element(By.XPATH, PageLocators.SECTION_FILLING).click()

        # Явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.SECTION_FILLING))
        )

        # Проверка на присутствие в классах элемента - значения "current", показывающего, что раздел выбран
        assert "current" in driver.find_element(By.XPATH, PageLocators.SECTION_FILLING).get_attribute("class")