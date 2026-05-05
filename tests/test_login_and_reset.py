import time
from pages.login_page import LoginPage
from pages.reset_db_page import ResetDBPage
from dotenv import load_dotenv
import os

load_dotenv()

def test_login_and_reset(driver, base_url):
    
   
    
    # Шаг 1: Авторизация на главной странице
    print("\n Выполняем вход...")
    login_page = LoginPage(driver, base_url)
    login_page.open()  
    login_page.fill_phone(os.getenv("TEST_PHONE"))
    login_page.fill_password(os.getenv("TEST_PASSWORD"))
    login_page.submit()
    time.sleep(3)  
    
    
    # Шаг 2: Переход на страницу /tests
    print("\n  Переходим на страницу /tests...")
    driver.get(base_url + "/tests")
    time.sleep(2)
    print("   ✅ Страница /tests открыта")
    
    # Шаг 3: Сброс БД
    print("\n Сбрасываем базу данных...")
    reset_page = ResetDBPage(driver, base_url)
    reset_page.reset_database()
   
    
    # Шаг 4: Создание администратора
    print("\n Создаём администратора...")
    reset_page.create_admin()
   
    
    