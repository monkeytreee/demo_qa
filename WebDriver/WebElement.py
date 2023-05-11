from time import sleep

from WebDriver.WebBase import WebBase


class WebElement(WebBase):

    def __init__(self, element, driver):
        super().__init__()
        self.element = element
        self.driver = driver

    def __getattr__(self, item):
        return getattr(self.element, item)

    def click(self):
        self.move_to_element()
        sleep(1)
        self.element.click()
        self.wait_interactive_ready_state()
        return self