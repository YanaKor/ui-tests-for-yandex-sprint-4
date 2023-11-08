import allure
import pytest

from pages.order_page import OrderPage
from test_data.data import Urls, UserInfo, OrderInfo, Date, Titles, IncorrectUser


class TestOrderPage:
    @allure.suite('Заказ самоката')
    @allure.title('Успешный заказ самоката')
    @allure.description('Заказ самоката по кнопке "Заказать" вверху страницы')
    def test_order_from_button_in_header(self, setup):
        order_page = OrderPage(setup)
        order_page.click_on_order_button_in_header()
        order_page.fill_info_about_customer(UserInfo.get_name(), UserInfo.get_surmane(), UserInfo.get_address(),
                                            OrderInfo.STATION[0], UserInfo.get_phone_number())
        order_page.click_on_next_button()
        order_page.fill_rent_info(Date.get_today_date(), OrderInfo.PERIOD_OF_RENT, UserInfo.get_text_comment())
        order_page.click_on_order_button()
        order_page.approve_order()
        order_page.check_success_order(Titles.SUCCESSFUL_ORDER)

    @allure.suite('Заказ самоката')
    @allure.title('Успешный заказ самоката')
    @allure.description('Заказ самоката по кнопке "Заказать" внизу страницы')
    def test_order_in_bottom(self, setup):
        order_page = OrderPage(setup)
        order_page.click_on_order_button_in_header()
        order_page.fill_info_about_customer(UserInfo.get_name(), UserInfo.get_surmane(), UserInfo.get_address(),
                                            OrderInfo.STATION[1], UserInfo.get_phone_number())
        order_page.click_on_next_button()
        order_page.fill_rent_info(Date.get_today_date(), OrderInfo.PERIOD_OF_RENT, UserInfo.get_text_comment())
        order_page.click_on_order_button()
        order_page.approve_order()
        order_page.check_success_order(Titles.SUCCESSFUL_ORDER)

    @allure.suite('Заказ самоката')
    @allure.title('Успешный заказ самоката')
    @allure.description('Заказ самоката по прямой ссылке')
    def test_fill_info_about_order(self, setup):
        order_page = OrderPage(setup)
        order_page.go_to_url(Urls.ORDER_URL)
        order_page.click_on_order_button_in_header()
        order_page.fill_info_about_customer(UserInfo.get_name(), UserInfo.get_surmane(), UserInfo.get_address(),
                                            OrderInfo.STATION[2], UserInfo.get_phone_number())
        order_page.click_on_next_button()
        order_page.fill_rent_info(Date.get_today_date(), OrderInfo.PERIOD_OF_RENT, UserInfo.get_text_comment())
        order_page.click_on_order_button()
        order_page.approve_order()
        order_page.check_success_order(Titles.SUCCESSFUL_ORDER)

    @allure.suite('Заказ самоката')
    @allure.title('Некорректный заказ самоката')
    @allure.description('Проверка заказа самоката с некорректными данными')
    @pytest.mark.parametrize('name, last_name, address, phone, error_message',
                             (IncorrectUser.NAME, IncorrectUser.SURNAME, IncorrectUser.ADDRESS, IncorrectUser.PHONE),
                             ids=['incorrect_name', 'incorrect_last_name', 'incorrect_address', 'incorrect_phone'])
    def test_fill_incorrect_data_in_order_form(self, setup, name, last_name, address, phone, error_message):
        order_page = OrderPage(setup)
        order_page.go_to_url(Urls.ORDER_URL)
        order_page.click_on_order_button_in_header()
        order_page.fill_info_about_customer(name, last_name, address, OrderInfo.STATION[0], phone)
        order_page.check_warning_message(error_message)
