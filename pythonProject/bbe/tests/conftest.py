import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def init_driver(request):
    # Инициализация драйвера
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def base_url():
    return 'https://demo.yookassa.ru/'

@pytest.fixture(scope="class")
def product_ids():
    return ['253354771', '253354830']

# @pytest.fixture(scope="class")
# def product_id():
#     return ['253354771']
