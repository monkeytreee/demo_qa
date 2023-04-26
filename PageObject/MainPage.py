from selenium.webdriver.common.by import By

from PageObject.AlertsFramesWindows.AlertsFramesWindowsPage import AlertsFramesWindowsPage
from PageObject.BasePage import BasePage
from PageObject.Elements.ElementsPage import ElementsPage
from PageObject.Forms.FormsPage import FormsPage
from PageObject.Interactions.InteractionsPage import InteractionsPage
from PageObject.Widgets.WidgetsPage import WidgetsPage


class MainPage(BasePage):
    EXPECTED_MAIN_TITLE = 'DEMOQA'
    SELENIUM_CERTIFICATION_TRAINING_BANNER = '.home-banner'
    ELEMENTS_BTN = '.category-cards .card:nth-of-type(1)'
    FORMS_BTN = '.category-cards .card:nth-of-type(2)'
    WIDGETS_BTN = '.category-cards .card:nth-of-type(3)'
    INTERACTIONS_BTN = '.category-cards .card:nth-of-type(4)'
    BOOK_STORE_APPS_BTN = '.category-cards .card:nth-of-type(5)'
    ALERTS_FRAMES_WINDOWS_BTN = '.category-cards .card:nth-of-type(6)'

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.__driver = driver

    def elements_btn_click(self):
        elements_btn = self.__driver.find_element(By.CSS_SELECTOR, self.ELEMENTS_BTN)
        elements_btn.click()
        return ElementsPage(self.__driver)

    def forms_btn_click(self):
        forms_btn = self.__driver.find_element(By.CSS_SELECTOR, self.FORMS_BTN)
        forms_btn.click()
        return FormsPage(self.__driver)

    def alert_frames_windows_btn_click(self):
        alert_frames_windows_btn = self.__driver.find_element(By.CSS_SELECTOR, self.ALERTS_FRAMES_WINDOWS_BTN)
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
        book_store_app_btn = self.__driver.find_element(By.CSS_SELECTOR, self.BOOK_STORE_APPS_BTN)
        book_store_app_btn.click()
        return ElementsPage(self.__driver)
