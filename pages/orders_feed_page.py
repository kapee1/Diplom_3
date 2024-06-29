from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.orders_feed_locators import OrdersFeedLocators
import allure


class FeedPage(BasePage):
    @allure.step('Клик по последнему заказу в ленте заказов')
    def click_on_last_order_in_feed(self):
        self.click(OrdersFeedLocators.last_order_in_feed_locator)

    @allure.step('Отображается ли окно созданного заказа')
    def is_order_window_displayed(self):
        return self.is_element_displayed(OrdersFeedLocators.order_window_locator)

    @allure.step('Получить номер последнего заказа из ленты')
    def get_last_order_numbers_in_feed(self):
        return self.get_text(OrdersFeedLocators.last_order_numbers_in_feed_list)

    @allure.step('Получить количество всех оформленных заказов ')
    def get_number_of_all_orders(self):
        return self.get_text(OrdersFeedLocators.counter_of_all_time_orders_locator)

    @allure.step('Получить количество заказов оформленных сегодня')
    def get_number_of_today_orders(self):
        return self.get_text(OrdersFeedLocators.counter_of_today_orders_locator)

    @allure.step('Дождаться появления заказа в списке "В работе"')
    def wait_order_in_work_list(self, order_number):
        WebDriverWait(self.driver, 20).until(expected_conditions.text_to_be_present_in_element
                                             (OrdersFeedLocators.last_orders_in_work_list_locator, order_number))

    @allure.step('Получить номер последнего заказа из списка "В работе"')
    def get_number_order_in_work_list(self):
        return self.get_text(OrdersFeedLocators.last_orders_in_work_list_locator)
