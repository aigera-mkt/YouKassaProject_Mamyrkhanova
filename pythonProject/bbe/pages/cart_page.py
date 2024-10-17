import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для формы айтема
    def product_form_locator_cart(self, product_id):
        return By.XPATH, f'//div[@data-product-id="{product_id}"]'

    # Локатор для "плюсика" на странице корзины
    def increase_item_locator(self, product_id):
        return (
            By.XPATH, f'//div[@data-product-id="{product_id}"]//button[contains(@class, "counter-button button button_size-s is-count-up ")]')
    #Локатор для минусика на странице корзины
    def decrease_item_locator(self, product_id):
        return (
            By.XPATH, f'//div[@data-product-id="{product_id}"]//button[contains(@class, "counter-button button button_size-s is-count-down ")]')

    # Локатор иконки "корзина" на удаление
    def cart_delete_icon_locator(self, product_id):
        return By.XPATH, f'//div[@data-product-id="{product_id}"]//div[@class="item-delete"]'
    #Локатор иконки корзина в форме товара
    def add_item_cart_page_locator(self, product_id):
        return (
            By.XPATH, f'//form[@data-product-id="{product_id}"]//button[contains(@class, "button add-cart-counter__btn")]')

    #Локатор для кнопки оформить заказ
    def order_button_locator(self):
        return By.XPATH, f'//button[contains(@class,"button button_size-l button_wide") and contains(text(), "Оформить заказ") ]'

    # Метод для открытия главной страницы (или другой нужной страницы)
    def open_cart_page(self):
        self.open_page('/cart_items')

    #Метод по добавлению товара из cart_page с пустой корзины:
    def add_item_cart_page(self,product_id):
        locator_item = self.add_item_cart_page_locator(product_id)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_item))
        basket_icon_cart_page = self.find_element(locator_item)
        basket_icon_cart_page.click()

    # Метод для добавления айтема через "плюсик"
    def plus_item_click(self, product_id):
        #Найти элемент плюсик
        product_increase_locator = self.increase_item_locator(product_id)
        product_increase = self.find_element(product_increase_locator)
        #Кликнуть на плюсик
        product_increase.click()
    #Удаление товара через минус
    def minus_item_click(self, product_id):
        #Найти элемент плюсик
        product_decrease_locator = self.decrease_item_locator(product_id)
        product_decrease = self.find_element(product_decrease_locator)
        #Кликнуть на плюсик
        product_decrease.click()

    def delete_item_click(self, product_id):
        delete_item = self.find_element(self.cart_delete_icon_locator(product_id))
        delete_item.click()
    #Локатор, отображающий кол-во добавленного товара через плюс
    def get_product_quantity_locator(self, product_id):
        return By.XPATH,f'//div[@data-product-id="{product_id}"]//input[@class="counter-input form-control form-control_size-s"]'
    #Метод, отображающий кол-во добавленного товара через плюс
    def get_product_quantity(self,product_id):
        element_value = self.find_element(self.get_product_quantity_locator(product_id))
        return int(element_value.get_attribute("value"))

    def order_button_click(self):
        order_button = self.order_button_locator()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(order_button))
        order_button_element = self.find_element(order_button)
        time.sleep(3)
        order_button_element.click()


