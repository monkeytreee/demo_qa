class MainFormPage:
    # Константа с ожидаемым заголовком главной страницы
    EXPECTED_MAIN_TITLE = 'DEMOQA'

    def __init__(self, driver):
        self.driver = driver

    def get_main_title(self):
        # Получаем заголовок главной страницы
        return self.driver.title

    def verify_main_title(self, expected_main_title):
        # Проверяем, что заголовок главной страницы содержит ожидаемое значение
        actual_title = self.get_main_title()
        assert expected_main_title in actual_title, f"Ошибка: ожидаемый заголовок '{self.EXPECTED_MAIN_TITLE}', фактический заголовок '{actual_title}'"