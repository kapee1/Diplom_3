import pytest
from selenium import webdriver
import requests
import helpers
import urls


@pytest.fixture(scope='function', params=['Chrome', 'Firefox'])
def driver(request):
    driver = WebDriverFactory.get_driver(request.param)
    driver.maximize_window()
    driver.get(url=urls.main_url)
    yield driver
    driver.quit()


class WebDriverFactory:
    @staticmethod
    def get_driver(name):
        if name == 'Chrome':
            return webdriver.Chrome()
        elif name == 'Firefox':
            return webdriver.Firefox()


@pytest.fixture(scope="function")
def create_and_delete_user():  # Создание и удаление пользователя
    user_data = helpers.generate_user_data()
    response = requests.post(urls.main_url + urls.CREATE_USER_API, json=user_data)
    yield user_data
    access_token = response.json()['accessToken']
    requests.delete(urls.main_url + urls.DELETE_USER_API, headers={'Authorization': access_token})
