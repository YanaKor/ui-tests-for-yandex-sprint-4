import allure
import pytest

from pages.main_page import MainPage


class TestQuestionsModule:

    @allure.suite('Вопросы о важном')
    @allure.title('Проверка выпадающего списка')
    @allure.description('Проверка соответствия вопроса-ответа в блоке "Вопросы о важном"')
    @pytest.mark.parametrize('num', [i for i in range(8)])
    def test_answers_on_important_questions(self, setup, num):
        main_page = MainPage(setup)
        main_page.get_list_of_questions_on_important_question(num)
        main_page.get_list_of_answers()
        main_page.check_answers_on_questions(num)
