import pytest
from selenium import webdriver
from helpers.locators import PageLocators

# Фикстура для настройки драйвера
@pytest.fixture
def driver():
    # Настроим WebDriver
    driver = webdriver.Chrome()

    # Раскрытие окна драйвера
    driver.maximize_window()

    # Открытие страницы тестового стенда
    driver.get(PageLocators.BASE_URL)

    yield driver

    # Закрытие браузера после теста
    driver.quit()
