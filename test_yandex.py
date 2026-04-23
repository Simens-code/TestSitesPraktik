import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Путь к Яндекс Браузеру 
path_to_yandex_browser = r"C:\Users\Семён\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"

# Путь к скачанному YandexDriver
path_to_yandex_driver = r"C:\TestSitesPraktik\drivers\yandexdriver.exe"

# Настройки
options = Options()
options.binary_location = path_to_yandex_browser

# Мобильная версия 
options.add_experimental_option("mobileEmulation", {
    "deviceMetrics": { "width": 390, "height": 844, "pixelRatio": 3 },
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
})

print("Запускаем Яндекс Браузер...")

# Указываем Selenium использовать YandexDriver
service = Service(executable_path=path_to_yandex_driver)
driver = webdriver.Chrome(service=service, options=options)

print("Открываем сайт...")
driver.get("https://cargo-test.mwire.ru")
time.sleep(20)

print("✅ Всё работает! Сайт открыт в Яндекс Браузере")
driver.quit()