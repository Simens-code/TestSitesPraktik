from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import time

class ResetDBPage(BasePage):
    """Страница сброса базы данных (/tests)"""

    def open(self):
        self.driver.get(self.base_url + "/tests")
        time.sleep(2)
    
    def reset_database(self):
        button = self.driver.find_element(By.CSS_SELECTOR, 'input[name="reset"]')
        button.click()

        WebDriverWait(self.driver, 3).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".alert-success"), "База данных сброшена")
        )
    
    def create_admin(self):
        button = self.driver.find_element(By.CSS_SELECTOR, 'input[name="create-admin"]')
        button.click()
        
        WebDriverWait(self.driver, 3).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".alert-success"), "Администратор создан")
        )