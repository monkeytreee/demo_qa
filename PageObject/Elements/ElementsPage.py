from PageObject.BasePage import BasePage


class ElementsPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.__driver = driver
        self.header = ".main-header"
        self.header_txt = "Elements"
