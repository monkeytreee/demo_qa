from selenium import webdriver
from WebDriver.WebBase import WebBase
from selenium.webdriver.firefox.service import Service


class WebDriver(WebBase):

    def __init__(self):
        super().__init__()
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--start-maximized")
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        driver_path = '/Users/Documents/geckodriver'
        self.service = Service(executable_path=driver_path)
        self.driver = webdriver.Firefox(service=self.service, options=self.options, desired_capabilities=self.capabilities)

    def __getattr__(self, item):
        return getattr(self.driver, item)
