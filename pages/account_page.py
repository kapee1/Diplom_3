import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    @allure.step('Кликаем по кнопке "История заказов"')
    def click_on_order_history_button(self):
        self.click(AccountPageLocators.order_history_button_locator)

    @allure.step('Кликаем по кнопке "Выход"')
    def click_on_log_out_button(self):
        self.click(AccountPageLocators.log_out_button_locator)
        self.wait_until_element_is_invisible(AccountPageLocators.log_out_button_locator)

    @allure.step('Получаем номер последнего заказа из истории заказов')
    def get_number_of_last_order(self):
        return self.get_text(AccountPageLocators.last_order_number_in_history_locator)
