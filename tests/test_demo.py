import pytest

from PageObject.MainPage import MainPage


class TestDemo:
    DEMOQA_URL = 'https://demoqa.com'

    @pytest.fixture(scope='function', autouse=True)
    def open_main_page(self, driver):
        driver.get(self.DEMOQA_URL)

    def test_main_title(self, driver):
        main_form_page = MainPage(driver)
        main_form_page.verify_main_title(main_form_page.EXPECTED_MAIN_TITLE)
