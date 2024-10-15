import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bbe.pages.start_page import StartPage
from bbe.pages.cart_page import CartPage
from bbe.pages.order_page import OrderPage


@pytest.mark.usefixtures("init_driver", "base_url","product_ids")
class TestAddToCart:
    def test_add_product_to_cart(self, base_url, product_ids):
        # Инициализация страницы
        start_page = StartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # Сохраняем текущий url стартовой страницы
        current_url = self.driver.current_url

        # ID продукта, который хотим добавить в корзину
        #product_ids = ['253354771', '253354830','253355137']

        # Добавление продукта в корзину
        for product_id in product_ids:
            start_page.add_product_to_cart(product_id)
            time.sleep(3)
        # Проверка, что товар добавлен в корзину
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"

        #Переходим на страницу корзины
        start_page.click_basket()
        time.sleep(3)
        # Ожидание изменения URL
        new_url = self.driver.current_url
        #Проверка перехода на новый URL
        assert new_url != current_url
@pytest.mark.usefixtures("init_driver", "base_url", "product_ids")
class TestCartOperations:
    def test_cart_operations(self, base_url, product_ids):
        # Инициализация страницы
        cart_page = CartPage(self.driver)
        # Открытие страницы корзины
        cart_page.open_cart_page()
        # Добавление продукта в корзину
        for product_id in product_ids:
            cart_page.add_item_cart_page(product_id)

        #Добавление товара через плюсик
            cart_page.plus_item_click(product_id)
            cart_page.plus_item_click(product_id)
            time.sleep(3)

        #Удаление товара через минус
            cart_page.minus_item_click(product_id)
            time.sleep(3)
        # Проверка, что количество равно 2
            assert cart_page.get_product_quantity(product_id) == 2, f"Product {product_id} quantity should be 2."
        #Добавляем товар
            cart_page.plus_item_click(product_id)
        # Удаление товара через иконку "trash"
            cart_page.delete_item_click(product_id)
            cart_page.driver.save_screenshot('screenshot1.png')

        # Добавляем товар
        product_id='253355137'
        cart_page.add_item_cart_page(product_id)
        time.sleep(5)
        # Кнопка оформить заказ
        cart_page.order_button_click()
@pytest.mark.usefixtures("init_driver", "base_url")
class TestNewOrder:
        def test_input_order(self, base_url):
        # Инициализация страницы корзины и заказа
            cart_page = CartPage(self.driver)
            order_page = OrderPage(self.driver)

            cart_page.open_cart_page()

            # Добавляем товар в корзину
            product_id = '253355137'
            cart_page.add_item_cart_page(product_id)

            # Нажимаем кнопку "Оформить заказ"
            cart_page.order_button_click()

            assert "order" in self.driver.current_url, "The order page did not open."

            # Открытие страницы заказа
            order_page.open_order_page()

            # Заполнить форму контактного телефона
            order_page.input_contact_number()

            #Проверка правильности заполнения поля контактного телефона
            assert order_page.get_contact_number() == "+7(926)555-11-22", "Contact number was not correctly filled."

            # Негативный сценарий, неверное заполнение населенного пункта
            order_page.input_wrong_location()
            # Подтвердить заказ
            order_page.submit_button_click()
            time.sleep(3)
            # Проверка наличия ошибки - алерт с текстом
            assert order_page.error_alert(), "Alert of location error is not displayed"
            time.sleep(3)
            #Очищаем поле населенного пункта
            order_page.input_location_clear()
            # Заполняем форму населенного пункта
            order_page.input_location_value()
            # Доставка курьером
            order_page.delivery_by_curier()
            time.sleep(3)
            # Проверка, что доставка курьером выбрана
            assert order_page.is_delivery_by_curier_selected(), "Courier delivery was not selected."

            # ФИО
            order_page.full_name()
            #Подтвердить заказ
            order_page.submit_button_click()

            # Проверка перехода на новый url
            expected_url_part = "order"
            current_url = self.driver.current_url  # Получаем текущий URL
            print(f"Current URL: {current_url}")
            assert expected_url_part in self.driver.current_url, f"The URL did not change as expected"
            time.sleep(5)
            # Проверка перехода на новый url с платежом
            expected_url_part = "payments"
            current_url = self.driver.current_url  # Получаем текущий URL
            print(f"Current URL: {current_url}")
            assert expected_url_part in self.driver.current_url, f"The URL did not change as expected"

