import time
import pytest
from selenium import webdriver


from SELENIUM import *
from S_F import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Change to your preferred browser driver
    yield driver
    driver.quit()



class TestSauseDemo:

    def test_login_p(self):  # test positive login
        url = 'https://www.saucedemo.com/'
        driver = get_driver(url)
        time.sleep(3)
        actual = test_login(driver)
        time.sleep(3)
        assert url != actual.url
        time.sleep(3)

    def test_correct_sort_by_price(self):
        url = 'https://www.saucedemo.com/'
        driver = get_driver(url)
        actual = test_sorting(driver)
        assert actual, "sorting didn't work"

    def test_images_match(self):
        url = 'https://www.saucedemo.com/'
        driver = get_driver(url)
        actual = self.test_images_match(driver)
        assert actual, "images don't match"