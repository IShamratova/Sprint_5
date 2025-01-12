import random
import string
import secrets
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.data import TestData
from helpers.locators import PageLocators


def generate_random_email(f_name):
    # Генерация случайного имени и фамилии
    last_name = random.choice(TestData.LAST_NAMES)

    if f_name[len(f_name) - 1] == "a":
        last_name = last_name + "a"

    # Генерация номера когорты (например, от 1 до 50)
    cohort_number = random.randint(1, 50)

    # Случайное число (например, от 0 до 999)
    number = random.randint(100, 999)

    # Случайный домен из списка
    email_domain = random.choice(TestData.EMAIL_DOMAINS)

    # Формирование email
    email = f"{f_name}{last_name}{cohort_number}{number}@{email_domain}"
    return email


def generate_secure_password():
    # Набор символов: буквы, цифры, специальные символы
    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    # Генерация пароля длиной 6 символов
    return ''.join(secrets.choice(characters) for _ in range(6))


def registration_of_new_user(driver, user_name, user_email, secure_password):
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

    driver.find_element(By.XPATH, PageLocators.LINK_REGISTER).click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_REGISTER))
    )
    time.sleep(1)

    # Поиск полей и их заполнение
    driver.find_element(By.XPATH, PageLocators.INPUT_NAME).send_keys(user_name)
    driver.find_element(By.XPATH, PageLocators.INPUT_EMAIL).send_keys(user_email)
    driver.find_element(By.XPATH, PageLocators.INPUT_PASSWORD).send_keys(secure_password)
    time.sleep(1)

    # Поиск кнопки "Зарегистрироваться" и клик по ней
    driver.find_element(By.XPATH, PageLocators.BUTTON_REGISTER).click()
    time.sleep(1)


def authorization_of_registered_user(driver, user_email, secure_password):
    # Явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ENTER))
    )
    time.sleep(1)

    # Поиск полей и их заполнение
    driver.find_element(By.XPATH, PageLocators.INPUT_EMAIL).send_keys(user_email)
    driver.find_element(By.XPATH, PageLocators.INPUT_PASSWORD).send_keys(secure_password)
    time.sleep(1)

    driver.find_element(By.XPATH, PageLocators.BUTTON_ENTER).click()
    time.sleep(1)

    # Явное ожидание для загрузки страницы после входа
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.BUTTON_ORDER))
    )
    time.sleep(1)

    # Кликаем по кнопке "Личный Кабинет"
    driver.find_element(By.XPATH, PageLocators.BUTTON_P_PERSONAL_ACCOUNT).click()

    # Явное ожидание для загрузки страницы профиля
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, PageLocators.LINK_PROFILE))
    )
    time.sleep(1)

    # Проверка URL-адреса на соответствие профилю
    assert driver.current_url == TestData.BASE_URL + TestData.ROUTES["profile"]