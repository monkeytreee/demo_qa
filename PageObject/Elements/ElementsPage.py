from PageObject.MainWidgetsPanel import MainWidgetsPanel


class ElementsPage(MainWidgetsPanel):
    def __init__(self, driver):
        MainWidgetsPanel.__init__(self, driver)
        self.__driver = driver
