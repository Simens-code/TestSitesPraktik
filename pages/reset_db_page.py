from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

class ResetDBPage(BasePage):
   

    def open(self, url=""):
        
        full_url = self.base_url + url
        self.driver.get(full_url)
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='reset']"))
        )
        return self
    
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
        