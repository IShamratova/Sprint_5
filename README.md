# Sprint_5
**Автотесты для сервиса Stellar Burgers:**<br />
<br />
**В модуле tests:**<br />
В файле test_registration.py:<br />
Успешная регистрация - test_registration_success,<br />
Регистрация с некорректным паролем - test_registration_incorrect_password<br />
<br />
В файле test_login.py:<br />
Вход через кнопку «Личный кабинет» - test_login_through_enter_account_button,<br />
Вход по кнопке «Войти в аккаунт» - test_login_through_personal_account_button,<br />
Вход через кнопку в форме регистрации - test_login_through_register_page,<br />
Вход через кнопку в форме восстановления пароля - test_login_through_password_recovery_page,<br />
<br />
В файле test_logout.py:<br />
Выход по кнопке «Выйти» в личном кабинете - test_logout<br />
<br />
В файле test_passage.py:<br />
Переход по клику на «Конструктор» - test_passage_to_constructor,<br />
Переход по клику на логотип Stellar Burgers - test_passage_to_logo,<br />
Переход по клику на «Личный кабинет» - test_passage_to_personal_account,<br />
Переходы к разделам: «Булки» - test_passage_to_section_buns,<br />
Переходы к разделам: «Соусы» - test_passage_to_section_sauces,<br />
Переходы к разделам: «Начинки» - test_passage_to_section_filling<br />
<br />
**В модуле helpers:**<br />
В файле data.py представлены тестовые данные:<br />
Адрес тестового стенла - BASE_URL,<br />
Список путей URL - ROUTES,<br />
Список имен - FIRST_NAMES,<br />
Список фамилий - LAST_NAMES,<br />
Список доменов почтовых служб - EMAIL_DOMAINS,<br />
Тестовый email зарегистрированного пользователя - USER_EMAIL_FOR_LOGIN,<br />
Тестовый пароль зарегистрированного пользователя - SECURE_PASSWORD_FOR_LOGIN<br />
<br />
В файле methods.py:<br />
Генерация случайных значений email - generate_random_email,<br />
Генерация случайных паролей - generate_secure_password,<br />
Регистрация нового пользователя - registration_of_new_user,<br />
Авторизация зарегистрированного пользователя - authorization_of_registered_user<br />
<br />
В файле locators.py представлен перечень локаторов<br />
