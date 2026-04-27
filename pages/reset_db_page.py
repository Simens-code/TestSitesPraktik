from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ResetDBPage(BasePage):
    """Страница сброса базы данных (/tests)"""
    
    
    RESET_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    
    def reset_database(self):
        """Выполнить сброс базы данных"""
        
        self.click(self.RESET_BUTTON)
        
        
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        
        return self
    
    def is_reset_successful(self):
        """Проверить, что сброс прошёл успешно"""
        return self.is_element_present(self.ALERT_SUCCESS)