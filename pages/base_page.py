import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseObject:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_present(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    @allure.step('Ввод текста')
    def type(self, locator, text):
        self.is_visible(locator).send_keys(text)

    @allure.step('Нажать на кнопку')
    def click(self, locator):
        self.is_clickable(locator).click()

    @allure.step('Получение текста из локатора')
    def get_text(self, locator):
        return self.is_visible(locator).text

    @allure.step('Прокрутка')
    def scroll_down(self, locator):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", locator)

    @allure.step('Переход по ссылке')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Получение списка элементов')
    def get_list_of_elements(self, locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    @allure.step('Переход к новой вкладке')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
