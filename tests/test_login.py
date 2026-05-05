import time
from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()

def test_login(driver, base_url):
  
    print("\n Запуск теста авторизации")
    
    login_page = LoginPage(driver, base_url)
    login_page.open()
    print(" Страница  открыта")
    
    login_page.fill_phone(os.getenv("TEST_PHONE"))
    login_page.fill_password(os.getenv("TEST_PASSWORD"))
    login_page.submit()
    
    time.sleep(2)
    print(" Авторизация выполнена успешно")
