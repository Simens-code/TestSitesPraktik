import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.reset_db_page import ResetDBPage

@pytest.fixture
def driver():
    print("\nЗапуск браузера...")
    
    options = Options()
    options.binary_location = r"C:\Users\Студент\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    
    options.add_experimental_option("mobileEmulation", {
        "deviceMetrics": { "width": 390, "height": 844, "pixelRatio": 3 },
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    })
    
    service = Service("drivers/yandexdriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://cargo-test.mwire.ru"

def test_reset_database(driver, base_url):
    """Тест: авторизация + сброс базы данных"""
    
    print("\nЗапуск теста...")
    
    page = ResetDBPage(driver, base_url)
    page.open()
    page.reset_database()
    page.create_admin()
    
    time.sleep(2)
    print(" Тест завершён!")