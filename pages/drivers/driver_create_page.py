from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import time

class DriverCreatePage(BasePage):
    
    def fill_last_name(self, last_name):
        try:
            last_name_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Фамилия')] | //input[@name='last_name']"))
            )
            last_name_input.send_keys(last_name)
            print(f"Фамилия введена: {last_name}")
        except Exception as e:
            print(f"Ошибка при вводе фамилии: {e}")
    
    def fill_first_name(self, first_name):
        try:
            first_name_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Имя')] | //input[@name='first_name']")
            first_name_input.send_keys(first_name)
            print(f"Имя введено: {first_name}")
        except Exception as e:
            print(f"Ошибка при вводе имени: {e}")
    
    def fill_middle_name(self, middle_name):
        try:
            middle_name_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Отчество')] | //input[@name='middle_name']")
            middle_name_input.send_keys(middle_name)
            print(f"Отчество введено: {middle_name}")
        except:
            pass
    
    def fill_phone(self, phone):
        try:
            phone_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Номер телефона')] | //input[@name='phone']")
            phone_input.clear()
            phone_input.send_keys(phone)
            print(f"Телефон введён: {phone}")
        except Exception as e:
            print(f"Ошибка при вводе телефона: {e}")
    
    def fill_address(self, address):
        try:
            address_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Адрес')] | //input[@name='address']")
            address_input.send_keys(address)
            print(f"Адрес введён: {address}")
        except Exception as e:
            print(f"Ошибка при вводе адреса: {e}")
    
    def fill_password(self, password):
        try:
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input#password"))
            )
            password_input.send_keys(password)
            print(f"Пароль введён")
        except Exception as e:
            print(f"Ошибка при вводе пароля: {e}")
    
    def click_create_button(self):
        try:
            create_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
            )
            create_button.click()
            print("Кнопка 'Создать' нажата")
            time.sleep(2)
        except Exception as e:
            print(f"Ошибка при нажатии кнопки: {e}")
    
    def is_form_complete(self):
        errors = {}
        try:
            last_name = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Фамилия')] | //input[@name='last_name']").get_attribute("value")
            if not last_name:
                errors['last_name'] = 'Фамилия не заполнена'
            
            first_name = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Имя')] | //input[@name='first_name']").get_attribute("value")
            if not first_name:
                errors['first_name'] = 'Имя не заполнено'
            
            phone = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Номер телефона')] | //input[@name='phone']").get_attribute("value")
            if not phone:
                errors['phone'] = 'Телефон не заполнен'
            
            if errors:
                return False, errors
            return True, {}
        except Exception as e:
            return False, {'error': str(e)}