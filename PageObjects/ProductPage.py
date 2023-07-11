from selenium.webdriver.common.by import By
#from PageObjects.LoginPage import LoginPage
#from test_cases.hooks import setup_with_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    def __init__(self, setup_with_login):
        self.driver = setup_with_login
        
    user_text = "oxd-userdropdown-name"
    user_menu = "#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-header > div.oxd-topbar-header-userarea > ul > li > ul"
    #dropdown_element = "oxd-icon bi-caret-down-fill oxd-userdropdown-icon" #class
    
    def wait(self): 
        wait = WebDriverWait(self.driver, timeout=10)


    def get_user_text(self):
        return self.driver.find_element(By.CLASS_NAME, self.user_text).text
    
    def click_on_user(self):
        self.driver.find_element(By.CSS_SELECTOR, self.user_menu).click()

    '''
    def click_on_user(self, wait):
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.dropdown_element)))
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.dropdown_element)))
        self.driver.find_element(By.CLASS_NAME, self.dropdown_element).click()
    '''    

    def click_on_logout(self):
        self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-link").click()

    def get_login_text(self):
        return self.driver.find_element(By.CLASS_NAME, "oxd-text oxd-text--h5 orangehrm-login-title").text