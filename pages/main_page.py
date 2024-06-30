from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from seletools.actions import drag_and_drop
import allure


class MainPage(BasePage):
    @allure.step('Отображется ли номер заказа')
    def is_order_identifier_text_displayed(self):
        return self.is_element_displayed(MainPageLocators.order_identifier_text_locator)

    @allure.step('Клик по кнопке "создать заказ"')
    def click_on_create_order_btn(self):
        self.click(MainPageLocators.create_order_button_locator)
        self.wait_until_element_is_visible(MainPageLocators.order_identifier_text_locator)

    @allure.step('Отображается ли окно ингредиента')
    def is_ingredient_window_displayed(self):
        return self.is_element_displayed(MainPageLocators.ingredient_window_locator)

    @allure.step('Отображается ли заголовок окна игредиента')
    def is_header_ingredient_window_displayed(self):
        return self.is_element_displayed(MainPageLocators.header_ingredient_window_locator)

    @allure.step('Клик по игредиенту')
    def click_on_ingredient(self):
        self.click(MainPageLocators.ingredient_locator)

    @allure.step('Клик по кнопке перехода в личный профиль')
    def click_on_my_account_button(self):
        self.click(MainPageLocators.my_account_button_locator)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.click(MainPageLocators.constructor_button_locator)

    @allure.step('Клик по кнопке списка заказов')
    def click_on_order_list_button(self):
        self.click(MainPageLocators.order_list_button_locator)

    @allure.step('Отображается ли конструктор')
    def is_constructor_displayed(self):
        return self.is_element_displayed(MainPageLocators.constructor_text_locator)

    @allure.step('Отображается ли список заказов')
    def is_order_list_displayed(self):
        return self.is_element_selected(MainPageLocators.order_list_text_locator)

    @allure.step('Клик по кнопки закрытия окна игредиента')
    def close_ingredient_window(self):
        self.click(MainPageLocators.close_button_on_ingredient_window_locator)
        self.wait_until_element_is_invisible(MainPageLocators.ingredient_window_locator)

    @allure.step('Перетаскивание элемента в корзину для оформления заказа')
    def drag_and_drop_element_to_basket(self):
        draggable = self.wait_and_find_element(MainPageLocators.ingredient_locator)
        droppable = self.wait_and_find_element(MainPageLocators.basket_ingredients_locator)
        drag_and_drop(self.driver, draggable, droppable)

    @allure.step('Получение значения счетчика для ингредиента')
    def get_ingredient_counter_value(self):
        return self.get_text(MainPageLocators.ingredient_counter_locator)

    @allure.step('Создание нового заказа')
    def create_new_order(self):
        self.drag_and_drop_element_to_basket()
        self.click_on_create_order_btn()

    @allure.step('Клик по лого в хедере для возарата на главную')
    def click_on_logo_to_return_to_main(self):
        self.click(MainPageLocators.logo_in_header_locator)
        self.wait_until_element_is_visible(MainPageLocators.constructor_text_locator)

    @allure.step('Получить номер оформленного заказа')
    def get_number_of_created_order(self):
        self.wait_until_element_to_be_presented(MainPageLocators.loader_in_order_window_locator)
        return self.get_text(MainPageLocators.order_number_in_order_window)
