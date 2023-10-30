Проект предназначен для тестирования API https://qa-scooter.praktikum-services.ru/docs/

Используются библиотеки: 
    requests - отправка запросов
    json - парсить json
    pytest - для тестов
    allure - для отчетов

Описание тестов: 
    test_successful_registration_with_random_data - успешная регистрация
    test_register_using_same_credentials - пытаемся регнуться дважды с одними кредами
    test_register_new_courier_without_required_attribute - пытаемся регнуться без логина или пароля, этих полей вообще нет в запросе
    test_register_new_courier_with_empty_fields - пытаемся регнуться без логина или пароля, поля есть но с пустыми значениями
    test_register_new_courier_with_same_login - пытаемся регнуться с занятым логином

    test_successful_login - успешный вход
    test_login_without_required_attribute - пытаемся войти без указания логина или пароля
    test_login_with_typo - пытаемся войти с невалидными логином или паролем

    test_create_order_with_specific_color - создаем заказ с указанием цвета самоката
    test_get_order_with_filters - получаем заказ (ради быстродействия используем фильтр)