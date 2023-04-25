from PageObject.MainWidgetsPanel import MainWidgetsPanel


class WidgetsPage(MainWidgetsPanel):
    def __init__(self, driver):
        MainWidgetsPanel.__init__(self, driver)
        self.__driver = driver
