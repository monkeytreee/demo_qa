from selenium.webdriver.common.by import By

from PageObject.AlertsFramesWindows.AlertsFramesWindowsPage import AlertsFramesWindowsPage
from PageObject.Elements.ElementsPage import ElementsPage
from PageObject.Footer import Footer
from PageObject.Forms.FormsPage import FormsPage
from PageObject.Header import Header
from PageObject.Interactions.InteractionsPage import InteractionsPage
from PageObject.Widgets.WidgetsPage import WidgetsPage


class MainPage(Header, Footer):
    EXPECTED_MAIN_TITLE = 'DEMOQA'
    SELENIUM_CERTIFICATION_TRAINING_BANNER = ''
    ELEMENTS_BTN = ''
    FORMS_BTN = ''
    ALERT_FRAMES_WINDOWS_BTN = ''
    WIDGETS_BTN = ''
    INTERACTIONS_BTN = ''
    BOOK_STORE_APPLICATION_BTN = ''

    def __init__(self, driver):
        Header.__init__(self, driver)
        Footer.__init__(self, driver)
        self.__driver = driver

    def get_main_title(self):
        return self.__driver.title

    def verify_main_title(self, expected_main_title):
        actual_title = self.get_main_title()
        assert expected_main_title in actual_title, f"Error: Expected main title '{self.EXPECTED_MAIN_TITLE}', " \
                                                    f"actual title '{actual_title}'"

    def elements_btn_click(self):
        elements_btn = self.__driver.find_element(By.CSS_SELECTOR, self.ELEMENTS_BTN)
        elements_btn.click()
        return ElementsPage(self.__driver)

    def forms_btn_click(self):
        forms_btn = self.__driver.find_element(By.CSS_SELECTOR, self.FORMS_BTN)
        forms_btn.click()
        return FormsPage(self.__driver)

    def alert_frames_windows_btn_click(self):
        alert_frames_windows_btn = self.__driver.find_element(By.CSS_SELECTOR, self.ALERT_FRAMES_WINDOWS_BTN)
        alert_frames_windows_btn.click()
        return AlertsFramesWindowsPage(self.__driver)

    def widgets_btn_click(self):
        widgets_btn = self.__driver.find_element(By.CSS_SELECTOR, self.WIDGETS_BTN)
        widgets_btn.click()
        return WidgetsPage(self.__driver)

    def interactions_btn_click(self):
        interactions_btn = self.__driver.find_element(By.CSS_SELECTOR, self.INTERACTIONS_BTN)
        interactions_btn.click()
        return InteractionsPage(self.__driver)

    def book_store_app_btn_click(self):
        book_store_app_btn = self.__driver.find_element(By.CSS_SELECTOR, self.BOOK_STORE_APPLICATION_BTN)
        book_store_app_btn.click()
        return ElementsPage(self.__driver)
