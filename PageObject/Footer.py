from selenium.webdriver.common.by import By


class Footer:
    FOOTER = ''

    def __init__(self, driver):
        self.__driver = driver

    def get_footer_element(self):
        """Get footer element by locator"""
        return self.__driver.find_element(By.CSS_SELECTOR, self.FOOTER)
