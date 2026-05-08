from pages.base_page import BasePage

class MainPage(BasePage):
    
    def open(self):
        self.driver.get(self.base_url)
    
    def go_to_drivers(self):
        self.driver.get(self.base_url + "/drivers")