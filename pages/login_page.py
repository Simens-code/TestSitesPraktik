from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage          # ← оставить
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginPage(BasePage):

    def open(self):
        self.driver.get(self.base_url)
        time.sleep(2)

    def fill_phone(self, phone: str):
        phone_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='phone']"))
        )
        phone_input.send_keys(phone)
        print(" Телефон введён")
        
    def fill_password(self, password: str):
        password_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_input.send_keys(password)
        print("Пароль введён")

    def submit(self):
        login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]")
        login_button.click()
        print("Нажата кнопка 'Войти'")