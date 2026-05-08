import time
import random
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.drivers.drivers_list_page import DriversListPage
from pages.drivers.driver_create_page import DriverCreatePage

load_dotenv()

def test_add_new_driver(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.fill_phone(os.getenv("TEST_PHONE"))
    login_page.fill_password(os.getenv("TEST_PASSWORD"))
    login_page.submit()
    time.sleep(5)
    
    main_page = MainPage(driver, base_url)
    main_page.go_to_drivers()
    time.sleep(3)
    
    drivers_list = DriversListPage(driver, base_url)
    drivers_list.click_new_button()
    time.sleep(5)
    
    print(f"Текущий URL после нажатия новой кнопки: {driver.current_url}")
    driver.save_screenshot("after_click_new.png")
    
    driver_create = DriverCreatePage(driver, base_url)
    
    random_number = random.randint(1000, 9999)
    last_name = "Тестов"
    first_name = f"Водитель{random_number}"
    middle_name = "Тестович"
    phone = f"+7{random_number}123456"
    address = f"Тестовый адрес {random_number}"
    password = f"TestPassword{random_number}!"

    driver_create.fill_last_name(last_name)
    driver_create.fill_first_name(first_name)
    driver_create.fill_middle_name(middle_name)
    driver_create.fill_phone(phone)
    driver_create.fill_address(address)
    driver_create.fill_password(password)
    
    is_complete, errors = driver_create.is_form_complete()
    
    if is_complete:
        print("Все поля заполнены")
        driver_create.click_create_button()
    else:
        print("Не все поля заполнены:")
        for field, error in errors.items():
            print(f"  - {error}")
    
    time.sleep(3)
    driver.get(base_url + "/drivers")
    time.sleep(3)
    
    if drivers_list.is_driver_added(last_name):
        print(f"Водитель {last_name} {first_name} добавлен")
    else:
        print(f"Водитель {last_name} {first_name} не найден")