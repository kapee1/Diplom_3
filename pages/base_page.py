import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)
        self.wait_for_page_load(url)

    @allure.step('Получить текущий адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Найти и дождаться появляения элемента')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Найти элемент и получить текст')
    def get_text(self, locator):
        element = self.wait_and_find_element(locator)
        return element.text

    @allure.step('Скролл до элемента')
    def scroll(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        button = self.wait_until_element_is_clickable(locator)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Переключение драйвера на другую вкладку')
    def switch_driver(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Проверка на то, что элемент выбран')
    def is_element_selected(self, locator):
        self.wait_and_find_element(locator)
        return expected_conditions.element_selection_state_to_be(element=locator, is_selected=True)

    @allure.step('Ожидание доступности элемента для клика')
    def wait_until_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ждет загрузки страницы с указанным URL.')
    def wait_for_page_load(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Отображается ли элемент')
    def is_element_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()
