import allure

from pages.main_page import MainPage
from test_data.data import Titles


class TestMainPage:

    @allure.suite('Главная страница')
    @allure.title('Переход между страницами')
    @allure.description('Проверка перехода на страницу Яндекс.Дзен по нажатию на лого Яндекса')
    def test_transition_to_dzen_main_page(self, setup):
        main_page = MainPage(setup)
        main_page.click_on_yandex_logo()
        main_page.check_transition_to_dzen_main_page()

    @allure.suite('Главная страница')
    @allure.title('Переход между страницами')
    @allure.description('Проверка перехода на главную старницу по нажатию на лого Самоката')
    def test_transition_to_scooter_main_page(self, setup):
        main_page = MainPage(setup)
        main_page.click_on_scooter_logo()
        main_page.check_transition_to_scooter_main_page(Titles.HEADER_TEXT)
