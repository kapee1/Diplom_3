import urls
from pages.login_page import LoginPage
import allure


class TestPasswordRecovery:
    @allure.title('Открытие раздела восстановления пароля успешно')
    def test_open_password_recovery_page(self, driver):
        page = LoginPage(driver)
        page.open_page(urls.login_url)
        page.click_on_recover_password_link()

        assert page.get_current_url() == urls.recovery_page_url

    @allure.title('Ввод емайл и восстановление пароля успешно')
    def test_input_email_and_click_recovery_button(self, driver):
        page = LoginPage(driver)
        page.open_page(urls.login_url)
        page.fill_email_field('test@email.com')
        page.click_on_recover_password_link()

        assert page.get_current_url() == urls.recovery_page_url

    @allure.title('Клик по кнопке "Показать\скрыть пароль" выделяет поле пароль')
    def test_click_on_show_hide_button_highlight_password_field(self, driver):
        page = LoginPage(driver)
        page.open_page(urls.login_url)
        page.click_show_hide_password_button()

        assert page.is_password_field_active() is True
