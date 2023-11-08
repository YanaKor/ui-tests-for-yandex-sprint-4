from faker import Faker
import random
from datetime import date
from dataclasses import dataclass


class Urls:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_URL = 'https://qa-scooter.praktikum-services.ru/order'


@dataclass
class UserInfo:
    name: str
    last_name: str
    address: str
    phone: str
    comment: str

    @staticmethod
    def get_name():
        return Faker('ru_Ru').first_name()

    @staticmethod
    def get_surmane():
        return Faker('ru_Ru').last_name()

    @staticmethod
    def get_address():
        return random.choice(['Москва', 'Московская область']) + ', ' + 'ул. ' + Faker('ru_Ru').street_name()

    @staticmethod
    def get_phone_number():
        return '+7' + str(random.randint(1000000000, 9999999999))

    @staticmethod
    def get_text_comment():
        return Faker('ru_Ru').text()


class OrderInfo:
    STATION = ["Черкизовская", "Сокольники", "Медведково"]
    PERIOD_OF_RENT = 'двое суток'


class Date:
    @staticmethod
    def get_today_date():
        return date.today().strftime('%d.%m.%Y')


class Titles:
    HEADER_TEXT = "Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём"
    SUCCESSFUL_ORDER = 'Заказ оформлен'
    FIRST_NAME_ERROR = 'Введите корректное имя'
    LAST_NAME_ERROR = 'Введите корректную фамилию'
    ADDRESS_ERROR = 'Введите корректный адрес'
    PHONE_NUMBER_ERROR = 'Введите корректный номер'


class Questions:
    LIST_OF_QUESTIONS = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. "
        "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
        "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. "
        "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. "
        "Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    ]


class IncorrectUser:
    NAME = ['test', UserInfo.get_surmane(), UserInfo.get_address(), UserInfo.get_phone_number(), Titles.FIRST_NAME_ERROR]
    SURNAME = [UserInfo.get_name(), 'test', UserInfo.get_address(), UserInfo.get_phone_number(), Titles.LAST_NAME_ERROR]
    ADDRESS = [UserInfo.get_name(), UserInfo.get_surmane(), 'test', UserInfo.get_phone_number(), Titles.ADDRESS_ERROR]
    PHONE = [UserInfo.get_name(), UserInfo.get_surmane(), UserInfo.get_address(), 'test', Titles.PHONE_NUMBER_ERROR]
