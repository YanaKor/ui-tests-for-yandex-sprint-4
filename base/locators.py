from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS_TITLE = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")
    QUESTION_BLOCK = (By.XPATH, ".//*[contains(@id, 'accordion__heading')]") # список вопросов
    ANSWERS_BLOCK = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]") # список ответов

    ACCEPT_COOKIES = (By.XPATH, ".//button[@class='App_CookieButton__3cvqF' and text()='да все привыкли']") # кнопка подтверждения cookie
    SCOOTER_BUTTON = (By.XPATH, ".//div/a[@class='Header_LogoScooter__3lsAR']") # логотип скутер
    YANDEX_BUTTON = (By.XPATH, ".//div/a[@class='Header_LogoYandex__3TSOI']") # логотип яндекс
    DZEN_FIND_BUTTON = (By.XPATH, ".//button[text() ='Найти']") # копка найти на странице яндекс.дзен

    TEXT_ON_MAIN_PAGE = (By. XPATH, "//div[contains(text(), 'Самокат')]") # текст


class OrderPageLocators:
    NAME_FIELD = (By.XPATH, ".//*[@placeholder='* Имя']") # поле заполения имени
    LAST_NAME_FIELD = (By.XPATH, ".//*[@placeholder='* Фамилия']") # поле заполения фамилии
    ADDRESS_FIELD = (By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']") # поле заполения адреса
    METRO_FIELD = (By.XPATH, ".//*[@placeholder='* Станция метро']") # поле заполения
    SELECT_METRO = By.XPATH, "//div[contains(text(),'{}')]"
    PHONE_NUMBER_FIELD = (By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']") # поле заполения номера телефона
    DATE_FIELD = (By.XPATH, ".//*[@placeholder='* Когда привезти самокат']") # поле заполения даты заказа
    ORDER_TIME_FIELD = (By.XPATH, ".//*[@class= 'Dropdown-arrow']") # поле заполения срока заказа
    RENT_PERIOD = (By.XPATH, ".//div[contains(text(),'{}')]")
    COLOR_OF_SCOOTER_CHECKBOX = (By.XPATH, ".//*[@id='grey']") # чекбокс выбора цвета самоката
    COMMENT_FOR_ORDER_FIELD = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']") # поле заполения комментария к заказу

    HEADER_ORDER_BUTTON = (By.XPATH, ".//*[contains(@class, 'Header_Nav')]//button[text()='Заказать']") # кнопка "Заказать" вверху
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']") # кнопка "заказать" внизу страницы
    NEXT_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Далее']") # кнопка далее
    ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']") # кнопка 'Заказать' в форме
    APPROVE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Да']") # подтверждение заказа

    ERROR_MESSAGE = By.XPATH, ".//div[contains(text(),'{}')]"
    ORDER_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]") # информация о статусе заказа
