from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from time import sleep
from selenium.webdriver.common.by import By
import pytest
from test_cases.hooks import setup

# Pro Pytest platí, že metody musí mít prefix test_ => tím Pytest zjistí, které metody jsou testovací
# a vše co je test_setup, test_login... bere jako test
class TestLogin:
    @pytest.mark.sanity
    def test_login(self, setup): #přidáme parametr setup, který vytváří driver a importujeme ho z hooks

        self.driver = setup

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        #sleep(3)
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        #sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        #driver.implicitly_wait(5)   

        #ověření metody test login
        title = self.driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb").text
        sleep(3)
        assert title == "Dashboard"
        sleep(3)

    #aby po testu nezůstal žádnej bordel, nebo se pouze driver zavřel
    def teardown_method(self): #self - předáváme této metodě instanci třídy TestLogin + pojmenujeme
                             #tuto metodu jen teardown, protože už to není test, stane se to po testu.
                             # aby to pytest nebral jako failed 
        self.driver.close()
        self.driver.quit()
        print("Test has been done")


