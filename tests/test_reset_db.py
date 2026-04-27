import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
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
    
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://cargo-test.mwire.ru"

def test_reset_database(driver, base_url):
    """Тест: авторизация + сброс базы данных"""
    
    print("\n🚀 Запуск теста...")
    
    # ----- Шаг 1: Открываем сайт и авторизуемся -----
    print("🔑 Открываем страницу авторизации...")
    driver.get(base_url)
    time.sleep(2)
    
    # Вводим телефон
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='tel'], input[name*='phone'], input[placeholder*='телефон'], input[placeholder*='Телефон']"))
    )
    phone_input.clear()
    phone_input.send_keys("9008001234")
    print("📱 Телефон введён")
    
    # Вводим пароль
    password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_input.clear()
    password_input.send_keys("uxENeov5GuvzkhxH")
    print("🔒 Пароль введён")
    
    # Нажимаем кнопку входа
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]")
    login_button.click()
    print("🔄 Нажата кнопка 'Войти'")
    
    # Ждём успешного входа
    time.sleep(3)
    print("✅ Авторизация выполнена")
    
    # ----- Шаг 2: Переходим на страницу сброса БД -----
    print("📂 Переход на страницу /tests...")
    driver.get(base_url + "/tests")
    time.sleep(2)
    
    # ----- Шаг 3: Сбрасываем БД -----
    # Ищем любую кнопку на странице (предполагаем, что это кнопка сброса)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    
    if buttons:
        print(f"🔘 Найдено кнопок: {len(buttons)}")
        for i, btn in enumerate(buttons):
            print(f"  Кнопка {i+1}: текст='{btn.text}'")
        
        # Нажимаем первую кнопку (скорее всего это сброс)
        buttons[0].click()
        print("🔄 Нажата кнопка сброса")
        
        # Подтверждаем alert (если он есть)
        try:
            alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
            alert.accept()
            print("✅ Alert подтверждён")
        except:
            print("⚠️ Alert не появился")
    else:
        print("❌ Кнопки не найдены!")
    
    time.sleep(2)
    print("✅ Тест завершён!")