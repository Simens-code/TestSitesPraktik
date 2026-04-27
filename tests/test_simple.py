import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def test_open_site():
    """Простой тест без фикстур"""
    print("\n🚀 Запуск браузера...")
    
    options = Options()
    options.binary_location = r"C:\Users\Семён\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    
    options.add_experimental_option("mobileEmulation", {
        "deviceMetrics": { "width": 390, "height": 844, "pixelRatio": 3 },
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    })
    
    service = Service("drivers/yandexdriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    
    print("📂 Открываем сайт...")
    driver.get("https://cargo-test.mwire.ru")
    time.sleep(3)
    
    print("✅ Сайт открыт!")
    driver.quit()