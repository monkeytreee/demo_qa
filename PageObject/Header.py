from selenium.webdriver.common.by import By


class Header:
    HEADER = ''

    def __init__(self, driver):
        self.__driver = driver

    def header_btn_click(self):
        """Click header element"""
        header_btn = self.__driver.find_element(By.CSS_SELECTOR, self.HEADER)
        header_btn.click()
