import pytest

from PageObject.MainPage import MainPage


class TestDemo:
    DEMOQA_URL = 'https://demoqa.com'

    @pytest.fixture(scope='function', autouse=True)
    def open_main_page(self, driver):
        driver.get(self.DEMOQA_URL)

    def test_elements_title(self, driver):
        main_page = MainPage(driver)
        elements_page = main_page.elements_btn_click()
        elements_page.verify_header()
