from selenium.webdriver.common.by import By


class MainPageLocators:
    logo_in_header_locator = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a"
    my_account_button_locator = By.XPATH, ".//p[text()='Личный Кабинет']"
    constructor_button_locator = By.XPATH, ".//p[text()='Конструктор']"
    order_list_button_locator = By.XPATH, ".//p[text()='Лента Заказов']"
    constructor_text_locator = By.XPATH, ".//h1[text()='Соберите бургер']"
    order_list_text_locator = By.XPATH, ".//h1[text()='Лента заказов']"
    close_button_on_ingredient_window_locator = By.XPATH, ("//button[@class='Modal_modal__close_modified__3V5XS "
                                                           "Modal_modal__close__TnseK']")
    header_ingredient_window_locator = By.XPATH, ".//h2[text()='Детали ингредиента']"
    ingredient_locator = By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']"
    ingredient_window_locator = By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']"
    basket_ingredients_locator = By.XPATH, ".//span[text()='Перетяните булочку сюда (верх)']"
    ingredient_counter_locator = By.XPATH, (".//img[@alt='Флюоресцентная булка R2-D3']/parent::a/div/p["
                                            "@class='counter_counter__num__3nue1']")
    create_order_button_locator = By.XPATH, ".//button[text()='Оформить заказ']"

    order_identifier_text_locator = By.XPATH, ".//p[text()='идентификатор заказа']"
    order_number_in_order_window = By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']/h2"
    loader_in_order_window_locator = By.XPATH, ".//div[@class='Modal_modal__P3_V5']"
