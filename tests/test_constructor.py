import urls
from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure


class TestConstructor:
    @allure.title('Клик по кнопке "конструктор" в хедере открывает раздел конструктор ')
    def test_click_on_constructor_btn_opens_constructor(self, driver):
        page = MainPage(driver)
        page.open_page(urls.main_url + urls.login_url)
        page.click_on_constructor_button()

        assert page.is_constructor_displayed()

    @allure.title('Клик по кнопке "список заказов" открывает раздел список заказов')
    def test_click_on_order_list_button_opens_order_list(self, driver):
        page = MainPage(driver)
        page.open_page(urls.main_url + urls.login_url)
        page.click_on_order_list_button()

        assert page.is_order_list_displayed()

    @allure.title('Клик по ингредиенту открывает окно свойств ингредиента')
    def test_click_on_ingredient_opens_window(self, driver):
        page = MainPage(driver)
        page.click_on_ingredient()

        assert page.is_header_ingredient_window_displayed()

    @allure.title('Закрытие окна ингредиента успешно')
    def test_close_ingredient_window(self, driver):
        page = MainPage(driver)
        page.click_on_ingredient()
        page.close_ingredient_window()

        assert page.is_ingredient_window_displayed() is False

    @allure.title('Добавление элемента в корзину успешно')
    def test_add_element_to_basket(self, driver):
        page = MainPage(driver)
        page.drag_and_drop_element_to_basket()

        assert page.get_ingredient_counter_value() == '2'

    @allure.title('Создание заказа авторизованным пользователем успешно')
    def test_create_order_by_auth_user(self, driver, create_and_delete_user):
        main = MainPage(driver)
        login = LoginPage(driver)
        user_data = create_and_delete_user
        login.authorization(user_data)
        main.create_new_order()

        assert main.is_order_identifier_text_displayed() is True
