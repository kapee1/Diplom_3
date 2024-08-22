from selenium.webdriver.common.by import By


class LoginPageLocators:
    recover_password_link_locator = By.XPATH, ".//a[text()='Восстановить пароль']"
    email_field_locator = By.XPATH, ".//input[@name='name']"
    not_active_password_field_locator = By.XPATH, ".//input[@type='password']"
    active_password_field_locator = By.XPATH, (".//div[@class='input pr-6 pl-6 input_type_text input_size_default "
                                               "input_status_active']")
    show_hide_password_button_locator = By.XPATH, ".//div[@class='input__icon input__icon-action']"
    login_button_locator = By.XPATH, ".//button[text()='Войти']"
