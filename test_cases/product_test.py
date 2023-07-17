from selenium import webdriver 
from time import sleep
import pytest
from test_cases.hooks import setup_with_login
from PageObjects.ProductPage import ProductPage

class TestProduct:
    @pytest.mark.positive_tests
    def test_product(self, setup_with_login):

        self.driver = setup_with_login
        product_page = ProductPage(self.driver)

        user = product_page.get_user_text()
        sleep(2)
        assert user == "Paul Collings"

    @pytest.mark.positive_tests
    def test_logout(self, setup_with_login):

        self.driver = setup_with_login
        product_page = ProductPage(self.driver)

        product_page.get_user_text()
        product_page.click_on_user()
        product_page.click_on_logout()
        
        get_login_text = product_page.get_login_text()
        
        sleep(2)

        assert get_login_text == "Login"

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

#test Git


    
