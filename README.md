Тестирование учебного сервиса «Яндекс.Самокат»

1. Фреймворк selenium
2. Браузер - Firefox 
3. Установить зависимости — pip install -r requirements.txt
4. Команда для запуска всех тестов — pytest .
5. Для формирования отчета в формате веб-страницы: allure serve allure_results

 Описание тестов: 
1. test_main_page.py - проверка переходов по логотипам
2. test_questions_module.py - проверка соответствия вопросов-ответов в блоке "Вопросы о важном"
3. test_order_page.py - проверка формы заказа самоката