import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

@pytest.fixture
def driver():
    """Фикстура драйвера - поддержка Yandex и Chrome"""
    browser = os.getenv("BROWSER", "Yandex").lower()
    mobile_emulation = os.getenv("MOBILE_EMULATION", "true").lower() == "true"
    
    options = Options()
    
    # Мобильная эмуляция
    if mobile_emulation:
        options.add_experimental_option("mobileEmulation", {
            "deviceMetrics": {"width": 390, "height": 844, "pixelRatio": 3},
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
        })
    
    # Настройка браузера
    if browser == "yandex":
        yandex_path = os.getenv("YANDEX_BROWSER_PATH")
        if not yandex_path:
            raise ValueError("YANDEX_BROWSER_PATH не задан в .env")
        options.binary_location = yandex_path
        from selenium.webdriver.chrome.service import Service
        service = Service("drivers/yandexdriver.exe")
        driver = webdriver.Chrome(service=service, options=options)
    
    elif browser == "chrome":
        driver = webdriver.Chrome(options=options)
    
    else:
        raise ValueError(f"Браузер '{browser}' не поддерживается. Используйте Yandex или Chrome")
    
    driver.implicitly_wait(int(os.getenv("DEFAULT_TIMEOUT", 10)))
    
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    """Базовый URL из .env"""
    return os.getenv("BASE_URL", "https://cargo-test.mwire.ru")