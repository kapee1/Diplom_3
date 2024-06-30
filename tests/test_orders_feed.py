import urls
from pages.orders_feed_page import FeedPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.main_page import MainPage
import allure


class TestFeedOrders:
    @allure.title('Клик по заказа открывает окно заказа')
    def test_click_on_order_opens_details_window(self, driver):
        page = FeedPage(driver)
        page.open_page(urls.feed_page_url)
        page.click_on_last_order_in_feed()

        assert page.is_order_window_displayed()

    @allure.title('Заказать пользователя отображается в ленте')
    def test_user_order_displayed_in_feed(self, driver, create_and_delete_user):
        login = LoginPage(driver)
        user_data = create_and_delete_user
        login.authorization(user_data)

        main = MainPage(driver)
        main.create_new_order()

        account = AccountPage(driver)
        account.open_page(urls.profile_url)
        account.click_on_order_history_button()
        last_order_number_in_account_history = account.get_number_of_last_order()

        feed = FeedPage(driver)
        feed.open_page(urls.feed_page_url)

        assert feed.get_last_order_numbers_in_feed() == last_order_number_in_account_history

    @allure.title('Новый заказ добавляется к счетику всех заказов')
    def test_new_order_counts_in_global_counter(self, driver, create_and_delete_user):
        login = LoginPage(driver)
        user_data = create_and_delete_user
        login.authorization(user_data)

        feed = FeedPage(driver)
        feed.open_page(urls.feed_page_url)
        orders_before = feed.get_number_of_all_orders()

        main = MainPage(driver)
        main.click_on_logo_to_return_to_main()
        main.create_new_order()

        feed.open_page(urls.feed_page_url)
        order_after = feed.get_number_of_all_orders()

        assert order_after > orders_before

    @allure.title('Новый заказа добавляется к счетчику сегодняшних заказов')
    def test_new_order_counts_in_today_counter(self, driver, create_and_delete_user):
        login = LoginPage(driver)
        user_data = create_and_delete_user
        login.authorization(user_data)

        feed = FeedPage(driver)
        feed.open_page(urls.feed_page_url)
        orders_before = feed.get_number_of_today_orders()

        main = MainPage(driver)
        main.click_on_logo_to_return_to_main()
        main.create_new_order()

        feed.open_page(urls.feed_page_url)
        order_after = feed.get_number_of_today_orders()

        assert order_after > orders_before

    @allure.title('Новый заказ попадает в список заказов "В работе"')
    def test_new_orders_appears_in_work_section(self, driver, create_and_delete_user):
        login = LoginPage(driver)
        user_data = create_and_delete_user
        login.authorization(user_data)

        main = MainPage(driver)
        main.click_on_logo_to_return_to_main()
        main.create_new_order()
        order_number = main.get_number_of_created_order()

        feed = FeedPage(driver)
        feed.open_page(urls.feed_page_url)
        feed.wait_order_in_work_list(order_number)

        assert order_number in feed.get_number_order_in_work_list()
