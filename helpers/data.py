class TestData:
    # Страница тестового стенда
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    # Список путей URL
    ROUTES = {
        "homepage": "/",
        "forgot-password": "forgot-password",
        "login": "/login",
        "profile": "/account/profile",
        "register": "/register"
    }

    # Список имен
    FIRST_NAMES = ["Ivan", "Anna", "Maria", "Petr", "Olga", "Artyom"]

    # Список фамилий
    LAST_NAMES = ["Ivanov", "Petrov", "Sidorov", "Smirnov", "Komarov", "Mikhaylov"]

    # Список доменов почтовых служб
    EMAIL_DOMAINS = ["yandex.ru", "mail.ru", "gmail.com", "example.com", "test.com"]

    # Тестовые данные для входа зарегистрированного пользователя
    USER_EMAIL_FOR_LOGIN = "ivan-ivanov6969@yandex.ru"
    SECURE_PASSWORD_FOR_LOGIN = "696969"