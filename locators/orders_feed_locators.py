from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    order_window_locator = By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"
    last_order_in_feed_locator = By.XPATH, ".//li[@class='OrderHistory_listItem__2x95r mb-6'][1]/a"

    counter_of_all_time_orders_locator = By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p"
    counter_of_today_orders_locator = By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"

    last_order_numbers_in_feed_list = By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[1]/a/div/p[1]"
    last_orders_in_work_list_locator = By.XPATH, (".//ul[@class='OrderFeed_orderListReady__1YFem "
                                                  "OrderFeed_orderList__cBvyi']/li[1]")
