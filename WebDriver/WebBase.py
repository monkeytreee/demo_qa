from time import sleep
from typing import Union

from selenium.common import NoSuchWindowException, WebDriverException, UnexpectedAlertPresentException, \
    NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 0.5
TIMEOUT_STEP = 0.5


class WebBase(object):
    def __init__(self):
        self.driver = None
        self.element = None

    def __custom_find_by(self, selenium_method: str, value: str, timeout: Union[float, int], wait_element_visibility=True):
        """
        Custom wrapper for selenium element search methods with support for timeouts and invisible element search
        """
        from WebDriver.WebElement import WebElement
        driver = self.driver if not isinstance(self, WebElement) else self.element

        if not isinstance(self, WebElement):
            self.wait_interactive_reade_state()

        def _expected_condition(_driver):
            prop = getattr(_driver, selenium_method)
            sleep(TIMEOUT_STEP)

            # Получаем список элементов
            elems = prop(value)

            # Если элементов не нашлось, падаем и пробуем снова
            if not elems:
                raise NoSuchElementException

            for el in elems:
                if el.is_displayed():
                    return el

                if wait_element_visibility is False:
                    return el

            raise NoSuchElementException

        wait = WebDriverWait(driver, timeout, TIMEOUT_STEP)
        try:
            return WebElement(wait.until(_expected_condition), self.driver)
        except Exception as e:
            print(e)
            return None

    def __custom_finds_by(
            self, selenium_method: str, value: str, timeout: Union[float, int], wait_element_visibility=True):
        """
        Custom wrapper for selenium element search methods with support for timeouts and invisible element search
        """
        from WebDriver.WebElement import WebElement
        driver = self.driver if not isinstance(self, WebElement) else self.elem

        if not isinstance(self, WebElement):
            self.wait_interactive_ready_state()

        def _expected_condition(_driver):
            result = []
            prop = getattr(_driver, selenium_method)
            sleep(TIMEOUT_STEP)
            elems = prop(value)

            if not elems:
                raise NoSuchElementException

            for el in elems:

                if el.is_displayed():
                    result.append(el)
                    continue

                if wait_element_visibility is False:
                    result.append(el)
                    continue

                if not result:
                    raise NoSuchElementException

                return result

        wait = WebDriverWait(driver, timeout, TIMEOUT_STEP)
        try:
            ret_results = []
            elements = wait.until(_expected_condition)
            for element in elements:
                ret_results.append(WebElement(element, self.driver))
            return ret_results
        except Exception as e:
            print(e)
            return []

    def wait_interactive_reade_state(self):
        """
        Wait till the page will get the ready status
        """
        def _interactive_method_state(driver):
            sleep(TIMEOUT_STEP)
            ready_state = driver.execute_script("return document.readyState")
            if 'interactive' in ready_state or 'complete' in ready_state:
                return True
            else:
                return False

        try:
            WebDriverWait(self.driver, timeout=TIMEOUT).until(
                _interactive_method_state, f"Page did'nt loaded in {TIMEOUT} seconds"
            )
        except (NoSuchWindowException, UnexpectedAlertPresentException, WebDriverException, TypeError):
            return

    def find_element_by_css_selector(self, value, timeout=TIMEOUT, wait_element_visibility=True):
        return self.__custom_find_by('find_element_by_css_selector', value, timeout, wait_element_visibility)

    def find_elements_by_css_selector(self, value, timeout=TIMEOUT, wait_element_visibility=True):
        return self.__custom_finds_by('find_elements_by_css_selector', value, timeout, wait_element_visibility)
