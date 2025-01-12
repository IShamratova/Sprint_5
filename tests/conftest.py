import pytest
from selenium import webdriver
from helpers.data import TestData

# Фикстура для настройки драйвера
@pytest.fixture
def driver():
    # Настроим WebDriver
    driver = webdriver.Chrome()

    # Раскрытие окна драйвера
    driver.maximize_window()

    # Открытие страницы тестового стенда
    driver.get(TestData.BASE_URL)

    yield driver

    # Закрытие браузера после теста
    driver.quit()
