from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import time

class DriversPage(BasePage):
    
    def open(self):
        self.driver.get(self.base_url + "/drivers")
        time.sleep(2)
    
    def click_new_button(self):
        new_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-sm.btn-success"))
        )
        new_button.click()
        time.sleep(2)
    
    def fill_last_name(self, last_name):
        last_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Фамилия'] | //label[contains(text(), 'Фамилия')]/following-sibling::input | //input[@name='last_name']"))
        )
        last_name_input.send_keys(last_name)
    
    def fill_first_name(self, first_name):
        first_name_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Имя'] | //label[contains(text(), 'Имя')]/following-sibling::input | //input[@name='first_name']")
        first_name_input.send_keys(first_name)
    
    def fill_middle_name(self, middle_name):
        try:
            middle_name_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Отчество'] | //label[contains(text(), 'Отчество')]/following-sibling::input | //input[@name='middle_name']")
            middle_name_input.send_keys(middle_name)
        except:
            pass
    
    def fill_phone(self, phone):
        phone_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Номер телефона'] | //label[contains(text(), 'Номер телефона')]/following-sibling::input | //input[@name='phone']")
        phone_input.clear()
        phone_input.send_keys(phone)
    
    def fill_address(self, address):
        address_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Адрес фактического проживания'] | //label[contains(text(), 'Адрес')]/following-sibling::input | //input[@name='address']")
        address_input.send_keys(address)
    
    def fill_password(self, password):
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Пароль'] | //label[contains(text(), 'Пароль')]/following-sibling::input | //input[@type='password']")
        password_input.send_keys(password)
    
    def click_create_button(self):
        create_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Создать')]"))
        )
        create_button.click()
        time.sleep(2)
    
    def is_driver_added(self, last_name, first_name):
        try:
            driver_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f"//td[contains(text(), '{last_name}')]"))
            )
            return True
        except:
            return False