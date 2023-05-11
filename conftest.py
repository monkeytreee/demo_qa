from datetime import datetime

import allure
import pytest

from PageObject.BasePage import BasePage
from WebDriver.WebDriver import WebDriver


@pytest.fixture(scope='session')
def page_object(driver):
    return BasePage(driver)


@pytest.fixture(scope='session')
def driver():
    return WebDriver().driver
    # options = Options()
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--disable-popup-blocking")
    # options.add_argument("--disable-notifications")
    # options.add_argument("--start-maximized")  # Запуск Firefox с максимальным размером окна
    #
    # driver_path = '/Users/Documents/geckodriver'
    # service = Service(executable_path=driver_path)
    # driver = webdriver.Firefox(service=service, options=options)
    #
    # driver.maximize_window()
    # driver.get("https://www.example.com")
    # yield driver
    # png = driver.get_screenshot_as_png()
    # allure.attach(png, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)
    #
    # driver.quit()


@pytest.fixture(scope='function', autouse=True)
def open_page(driver, page_object):
    driver.get("https://www.example.com")
    yield driver
    png = driver.get_screenshot_as_png()
    allure.attach(png, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)

    driver.quit()
