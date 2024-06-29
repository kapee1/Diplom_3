import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AccountPage(BasePage):
    @allure.step('Кликаем по кнопке "История заказов"')
    def click_on_order_history_button(self):
        self.click(AccountPageLocators.order_history_button_locator)

    @allure.step('Кликаем по кнопке "Выход"')
    def click_on_log_out_button(self):
        self.click(AccountPageLocators.log_out_button_locator)
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located
                                             (AccountPageLocators.log_out_button_locator))

    @allure.step('Получаем номер последнего заказа из истории заказов')
    def get_number_of_last_order(self):
        return self.get_text(AccountPageLocators.last_order_number_in_history_locator)
