from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import time

class DriversListPage(BasePage):
    
    def open(self):
        self.driver.get(self.base_url + "/drivers")
        time.sleep(2)
    
    def click_new_button(self):
        new_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-sm.btn-success"))
        )
        new_button.click()
        time.sleep(2)
    
    def is_driver_added(self, last_name):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f"//td[contains(text(), '{last_name}')]"))
            )
            return True
        except:
            return False