import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для поиска товара по data-product-id
    def product_form_locator(self, product_id):
        return By.XPATH, f'//form[@data-product-id="{product_id}"]'

    # Локатор для кнопки "В корзину" внутри формы продукта
    def add_to_cart_button_locator(self, product_id):
        return (
            By.XPATH, f'//form[@data-product-id="{product_id}"]//button[contains(@class, "product-preview__buy-btn")]')

    # Локатор для проверки успешного добавления в корзину (тоуст высплывающий)
    def cart_success_locator(self):
        return By.XPATH, '//div[contains(@class, "micro-alert-item")]'

    # Метод для добавления продукта в корзину
    def add_product_to_cart(self, product_id):
        # Найти форму продукта
        product_form = self.find_element(self.product_form_locator(product_id))

        # Навести на кнопку "В корзину"
        self.hover(self.add_to_cart_button_locator(product_id))

        # Кликнуть по кнопке "В корзину"
        self.click(self.add_to_cart_button_locator(product_id))

    # Метод для открытия главной страницы (или другой нужной страницы)
    def open_start_page(self):
        self.open_page()

    # Метод для проверки, что товар добавлен в корзину
    def is_product_added_to_cart(self):
        return self.find_element(self.cart_success_locator())

    # Локатор для кнопки с иконкой <корзина>
    def button_cart_locator(self):
        return By.XPATH, f'//a[contains(@class, "header__cart")]'

    # Метод по клику по иконке корзины

    def click_basket(self):
        locator_basket = self.button_cart_locator()
        element_button_basket = self.find_element(locator_basket)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_basket))
        element_button_basket.click()

