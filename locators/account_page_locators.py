from selenium.webdriver.common.by import By


class AccountPageLocators:
    order_history_button_locator = By.XPATH, ".//a[text()='История заказов']"
    log_out_button_locator = By.XPATH, ".//button[text()='Выход']"
    last_order_number_in_history_locator = By.XPATH, (".//ul[@class='OrderHistory_profileList__374GU "
                                                      "OrderHistory_list__KcLDB']/li[last()]/a/div/p[1]")
