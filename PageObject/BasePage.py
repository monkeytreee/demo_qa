from selenium.webdriver.common.by import By

from PageObject.MainWidgetsPanel import MainWidgetsPanel


class BasePage(MainWidgetsPanel):
    def __init__(self, driver):
        MainWidgetsPanel.__init__(self, driver)
        self.__driver = driver
        self.__header = str()
        self.__header_txt = str()

    @property
    def driver(self):
        return self.__driver

    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, value):
        if not value:
            pass
        else:
            self.__header = value

    @property
    def header_txt(self):
        return self.__header_txt

    @header_txt.setter
    def header_txt(self, value):
        if not value:
            pass
        else:
            self.__header_txt = value

    def verify_header(self, header_text=None):
        """
        Checks the title of the popup
        """
        header_text = self.__header_txt if not header_text else header_text
        header_elem = self.__driver.find_element(By.CSS_SELECTOR, self.__header)
        assert header_elem.text == header_text, \
            f"Header not as expected - {header_text}. Real header - {header_elem.text}"
