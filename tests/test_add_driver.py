import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.drivers_page import DriversPage
from dotenv import load_dotenv
import os
import random

load_dotenv()

def test_add_new_driver(driver, base_url):
    
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.fill_phone(os.getenv("TEST_PHONE"))
    login_page.fill_password(os.getenv("TEST_PASSWORD"))
    login_page.submit()
    time.sleep(3)
    
    drivers_page = DriversPage(driver, base_url)
    drivers_page.open()
    time.sleep(2)
    
    drivers_page.click_new_button()
    
    random_number = random.randint(1000, 9999)
    last_name = f"Тестов"
    first_name = f"Водитель{random_number}"
    middle_name = f"Тестович"
    phone = f"+7{random_number}123456"
    address = f"Тестовый адрес {random_number}"
    password = f"TestPassword{random_number}!"

    drivers_page.fill_last_name(last_name)
    drivers_page.fill_first_name(first_name)
    drivers_page.fill_middle_name(middle_name)
    drivers_page.fill_phone(phone)
    drivers_page.fill_address(address)
    drivers_page.fill_password(password)