import allure

from pages.base_page import BaseObject
from support.assertions import Assertions
from base.locators import MainPageLocators as Main
from test_data.data import Questions


class MainPage(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Нажатие на лого Яндекса')
    def click_on_yandex_logo(self):
        self.click(Main.YANDEX_BUTTON)

    @allure.step('Нажатие на лого Скутера')
    def click_on_scooter_logo(self):
        self.go_to_url('https://qa-scooter.praktikum-services.ru/order')
        self.click(Main.SCOOTER_BUTTON)

    @allure.step('Проверка открытия новой вкладки Яндекс.Дзен после нажатия на лого Яндекса')
    def check_transition_to_dzen_main_page(self):
        self.switch_to_new_tab()
        self.assert_equal(self.get_text(Main.DZEN_FIND_BUTTON), 'Найти')

    @allure.step('Проверка открытия главной страницы Яндекс.Самокат после нажатия на лого Самокат со страницы заказа')
    def check_transition_to_scooter_main_page(self, text):
        self.assert_equal(self.get_text(Main.TEXT_ON_MAIN_PAGE), text)

    @allure.step('Проверка открытия соответствующего ответа при нажатии на вопрос в разделе "Вопросы о важном"')
    def get_list_of_questions_on_important_question(self, num):
        self.scroll_down(Main.QUESTIONS_TITLE)
        list_of_questions = self.get_list_of_elements(Main.QUESTION_BLOCK)
        list_of_questions[num].click()

    @allure.step('Получение ответа на вопросы')
    def get_list_of_answers(self):
        answers = self.driver.find_element(*Main.ANSWERS_BLOCK).text
        return answers

    @allure.step('Проверка соответствия ответа на вопросы')
    def check_answers_on_questions(self, num):
        self.assert_check(Questions.LIST_OF_QUESTIONS[num], self.get_list_of_answers())
