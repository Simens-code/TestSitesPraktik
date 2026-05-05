import pytest
from pages.reset_db_page import ResetDBPage

def test_reset_database(driver, base_url):
    
    
   
    
    page = ResetDBPage(driver, base_url)
    page.open("/tests")  
    page.reset_database()
    page.create_admin()
    
    print(" Тест завершён")