import allure
from pages.base_page import BaseObject
from support.assertions import Assertions
from base.locators import OrderPageLocators as Order


class OrderPage(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Нажатие на кнопку "Заказать" вверху страницы')
    def click_on_order_button_in_header(self):
        self.click(Order.HEADER_ORDER_BUTTON)

    @allure.step('Нажатие на кнопку "Заказать" внизу страницы')
    def click_on_order_button_in_bottom(self):
        self.click(Order.BOTTOM_ORDER_BUTTON)

    @allure.step('Заполнение страницы "Для кого самокат"')
    def fill_info_about_customer(self, name, last_name, address, metro, phone_number):
        self.type(Order.NAME_FIELD, name)
        self.type(Order.LAST_NAME_FIELD, last_name)
        self.type(Order.ADDRESS_FIELD, address)
        self.type(Order.PHONE_NUMBER_FIELD, phone_number)
        self.select_metro(metro)

    @allure.step('Ввод станции метро')
    def select_metro(self, metro):
        self.type(Order.METRO_FIELD, metro)
        method, locator = Order.SELECT_METRO
        locator = method, locator.format(metro)
        self.driver.find_element(*locator).click()

    @allure.step('Клик на кнопку "Далее"')
    def click_on_next_button(self):
        self.click(Order.NEXT_BUTTON)

    @allure.step('Заполнение даты, когда привезти самокат')
    def fill_date_of_the_scooter_order(self, date):
        self.type(Order.DATE_FIELD, date)

    @allure.step('Выбор срока аренды')
    def choose_of_scooter_rental_period(self, period):
        self.click(Order.ORDER_TIME_FIELD)
        method, locator = Order.RENT_PERIOD
        locator = method, locator.format(period)
        self.driver.find_element(*locator).click()

    @allure.step('Выбор цвета самоката')
    def set_color_of_scooter(self):
        self.click(Order.COLOR_OF_SCOOTER_CHECKBOX)

    @allure.step('Заполнение комментария к заказу')
    def fill_comments_field(self, text):
        self.type(Order.COMMENT_FOR_ORDER_FIELD, text)

    @allure.step('Заполнение страницы "Про аренду"')
    def fill_rent_info(self, date, period, text):
        self.fill_date_of_the_scooter_order(date)
        self.choose_of_scooter_rental_period(period)
        self.set_color_of_scooter()
        self.fill_comments_field(text)

    @allure.step('Клик на кнопку "Заказать"')
    def click_on_order_button(self):
        self.click(Order.ORDER_BUTTON)

    @allure.step('Подтверждение оформления заказа')
    def approve_order(self):
        self.click(Order.APPROVE_BUTTON)

    @allure.step('Проверка успешного оформления заказа')
    def check_success_order(self, text):
        self.assert_check(text, self.get_text(Order.ORDER_TITLE))

    @allure.step('Проверка ошибки заполнения поля')
    def check_warning_message(self, text):
        method, locator = Order.ERROR_MESSAGE
        locator = method, locator.format(text)
        expected_text = self.driver.find_element(*locator).text
        self.assert_equal(expected_text, text)
