import allure

import urls
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestAccountPage:
    @allure.title('Клик по кнопке "Мой аккаунт" открывает профиль')
    def test_click_on_btn_my_account_opens_profile(self, driver):
        main = MainPage(driver)
        main.click_on_my_account_button()

        assert main.get_current_url() == urls.login_url

    @allure.title('Клик по кнопке "История заказов" открывает историю заказов')
    def test_open_orders_history(self, driver, create_and_delete_user):
        login = LoginPage(driver)
        account = AccountPage(driver)

        response, payload = create_and_delete_user
        email = payload['email']
        password = payload['password']

        login.authorization(email, password)
        account.open_page(urls.profile_url)
        account.click_on_order_history_button()

        assert account.get_current_url() == urls.order_history_url

    @allure.title('Выход из аккаунта')
    def test_logout_from_account(self, driver, create_and_delete_user):
        login = LoginPage(driver)
        account = AccountPage(driver)
        response, payload = create_and_delete_user
        email = payload['email']
        password = payload['password']
        login.authorization(email, password)
        login.open_page(urls.profile_url)
        account.click_on_log_out_button()

        assert account.get_current_url() == urls.login_url

