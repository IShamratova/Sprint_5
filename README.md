# Sprint_5
Автотесты для сервиса Stellar Burgers:<br />
<br />
в файле регистрация - registration.py:<br />
успешная регистрация - test_registration_success,<br />
регистрация и невалидным паролем - test_registration_incorrect_password<br />
<br />
в файле вход - login.py:<br />
вход через кнопку «Личный кабинет» - test_login_through_enter_account_button,<br />
вход по кнопке «Войти в аккаунт» - test_login_through_personal_account_button,<br />
вход через кнопку в форме регистрации - test_login_through_register_page,<br />
вход через кнопку в форме восстановления пароля - test_login_through_password_recovery_page,<br />
<br />
в файле выход - logout.py:<br />
выход по кнопке «Выйти» в личном кабинете - test_logout<br />
<br />
в файле переход - passage.py:<br />
переход по клику на «Конструктор» - test_passage_to_constructor,<br />
переход по клику на логотип Stellar Burgers - test_passage_to_logo,<br />
переход по клику на «Личный кабинет» - test_passage_to_personal_account,<br />
переходы к разделам: «Булки», «Соусы», «Начинки» - test_passage_to_sections<br />
<br />
в файле методы - methods.py:<br />
список имен - first_names,<br />
список фамилий - last_names,<br />
список доменов почтовых служб - email_domains,<br />
email зарегистрированного пользователя - user_email_for_login,<br />
пароль зарегистрированного пользователя - secure_password_for_login,<br />
генерация случайных значений email - generate_random_email,<br />
генерация случайных паролей - generate_secure_password,<br />
регистрация нового пользователя - registration_of_new_user,<br />
авторизация зарегистрированного пользователя - authorization_of_registered_user,<br />
<br />
в файле locators.py представлен перечень локаторов<br />
