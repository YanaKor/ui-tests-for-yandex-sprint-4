import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from test_data.data import Urls


@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    url = Urls.MAIN_URL
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    yield driver

    driver.quit()
