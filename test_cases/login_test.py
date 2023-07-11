from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from time import sleep
from selenium.webdriver.common.by import By
import pytest
from test_cases.hooks import setup
from PageObjects.LoginPage import LoginPage

# Pro Pytest platí, že metody musí mít prefix test_ => tím Pytest zjistí, které metody jsou testovací
# a vše co je test_setup, test_login... bere jako test
class TestLogin:
    @pytest.mark.sanity
    def test_login(self, setup): #přidáme parametr setup, který vytváří driver a importujeme ho z hooks

        self.driver = setup

        #budeme volat metody z LoginPage třídy
        #přístup k LoginPage třídě
        login_page = LoginPage(self.driver) #musíme samozřejmě importovat třídu LoginPage

        login_page.input_username("Admin")   #nyní když dáme tečku, vidíme, že máme přístup ke všem metodám ve třídě
        login_page.input_password("admin123")
        login_page.click_on_login()
        title = login_page.get_title_text()

        assert title == "Dashboard"
        sleep(3)

    #aby po testu nezůstal žádnej bordel, nebo se pouze driver zavřel
    def teardown_method(self): #self - předáváme této metodě instanci třídy TestLogin + pojmenujeme
                             #tuto metodu jen teardown, protože už to není test, stane se to po testu.
                             # aby to pytest nebral jako failed 
        self.driver.close()
        self.driver.quit()
        print("Test has been done")