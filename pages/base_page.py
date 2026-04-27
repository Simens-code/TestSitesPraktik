from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 10
        self.wait = WebDriverWait(driver, self.timeout)
    
    def open(self, url=""):
        """Открыть страницу"""
        full_url = self.base_url + url
        self.driver.get(full_url)
        return self
    
    def find_element(self, locator, timeout=None):
        """Найти элемент с ожиданием"""
        timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        """Кликнуть по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self
    
    def input_text(self, locator, text):
        """Ввести текст"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return self
    
    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text
    
    def is_element_present(self, locator, timeout=5):
        """Проверить наличие элемента без ошибки"""
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False