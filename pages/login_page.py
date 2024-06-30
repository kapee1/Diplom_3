import allure
import urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Клик по ссылке восстановленя пароля')
    def click_on_recover_password_link(self):
        self.click(LoginPageLocators.recover_password_link_locator)

    @allure.step('Заполнить поле электронный почти')
    def fill_email_field(self, email):
        self.wait_and_find_element(LoginPageLocators.email_field_locator).send_keys(email)

    @allure.step('Заполнить поле пароль')
    def fill_password_field(self, password):
        self.wait_and_find_element(LoginPageLocators.not_active_password_field_locator).send_keys(password)

    @allure.step('Клик по кнопке "войти"')
    def click_on_login_button(self):
        self.click(LoginPageLocators.login_button_locator)

    @allure.step('Клик по кнопке отображаения пароля')
    def click_show_hide_password_button(self):
        self.click(LoginPageLocators.show_hide_password_button_locator)

    @allure.step('Убедится, что поле "пароль" активно')
    def is_password_field_active(self):
        return self.wait_and_find_element(LoginPageLocators.active_password_field_locator).is_displayed()

    @allure.step('Авторизация пользователя')
    def authorization(self, user):
        self.open_page(urls.main_url + urls.login_url)
        self.fill_email_field(user['email'])
        self.fill_password_field(user['password'])
        self.click_on_login_button()
        self.wait_until_element_is_invisible(LoginPageLocators.email_field_locator)
