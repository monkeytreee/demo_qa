from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope='session')
def driver() -> webdriver:
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")  # Запуск Firefox с максимальным размером окна

    driver_path = '/Users/Documents/geckodriver'
    service = Service(executable_path=driver_path)
    driver = webdriver.Firefox(service=service, options=options)

    driver.maximize_window()
    driver.get("https://www.example.com")
    yield driver
    png = driver.get_screenshot_as_png()
    allure.attach(png, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)

    driver.quit()
