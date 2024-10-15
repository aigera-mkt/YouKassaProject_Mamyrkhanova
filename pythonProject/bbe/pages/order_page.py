import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для формы контакт номер
    def contact_number_locator(self):
        return By.ID, "client_phone"
    #Локатор формы населенного пункта
    def location_locator(self):
        return By.ID, "shipping_address_full_locality_name"
    #Локатор кнопки Подтвердить заказ
    def submit_button_locator(self):
        return By.XPATH, f'//*[@id="create_order"]'

    # Метод для открытия страницы заказа (или другой нужной страницы)
    def open_order_page(self):
        self.open_page('/new_order')
    #Метод для нахождения контакт  формы
    def input_contact_number(self):
         contact_number = self.contact_number_locator()
         element_contact_number = self.find_element(contact_number)
         element_contact_number.send_keys("+7(926)555-11-22")
    #Метод по заполнению формы настеленного пункта
    def input_location_value(self):
        location = self.location_locator()
        element_location = self.find_element(location)
        #Ввести новое значение:
        element_location.send_keys("г Ростов-на-Дону, Ростовская обл.")

    def input_location_clear(self):
        location = self.location_locator()
        element_location = self.find_element(location)
        #element_location.click()
        # Используем JavaScript для клика по элементу
        self.driver.execute_script("arguments[0].click();", element_location)
        # Выделить весь текст в инпуте и удалить его
        element_location.send_keys(Keys.CONTROL + "a")
        element_location.send_keys(Keys.BACKSPACE)

    def input_wrong_location(self):
        location = self.location_locator()
        element_location = self.find_element(location)
        element_location.clear()
        element_location.send_keys("г.Алматы")
     #Находим сообщение об ошибке по неверному вводу населенного пункта
    def error_alert(self):
         error_alert_element = self.find_element((By.XPATH, "//*[@id='delivery-location-not-valid']"))
         return error_alert_element.is_enabled()
    #Метод по выбору доставки курьером
    def delivery_by_curier(self):
        delivery_element = self.find_element((By.XPATH, "//*[@id='delivery_variants']/div[2]/label[2]/span[1]/span"),10)
        delivery_element.click()

    # Метод по заполнению ФИО
    def full_name(self):
        full_name_element = self.find_element((By.XPATH, "//*[@id='client_name']"),10)
        full_name_element.send_keys("Мамырханова Айгерим Талгатовна")

    # Метод для проверки выбора доставки курьером
    def is_delivery_by_curier_selected(self):
        try:
            delivery_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='order_delivery_variant_id_7870784']"))
            )
            return delivery_element.is_selected()  # Проверка, выбран ли элемент
        except Exception as e:
            print(f"An error occurred while checking delivery selection: {e}")
            return False

    # Метод для получения контактного номера
    def get_contact_number(self):
        try:
            contact_number_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "client_phone"))
                )
            return contact_number_element.get_attribute('value')  # Получение значения поля
        except Exception as e:
            print(f"An error occurred while getting contact number: {e}")
            return None  # Вернуть None, если произошла ошибка

    # Клик по кнопке Подтвердить заказ
    def submit_button_click(self):
        submit_button = self.submit_button_locator()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(submit_button))
        submit_button_element = self.find_element(submit_button)
        submit_button_element.click()