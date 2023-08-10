from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.ui import Select

class ProductPage:

    def __init__(self, setup_with_login):
        self.driver = setup_with_login
        
    user_text = "oxd-userdropdown-name"
    user_menu = "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
    
    def wait(self): 
        wait = WebDriverWait(self.driver, timeout=10)


    def get_user_text(self):
        return self.driver.find_element(By.CLASS_NAME, self.user_text).text
    
    def click_on_user(self):
        sleep(10)
        self.driver.find_element(By.XPATH, self.user_menu).click()

    def click_on_logout(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()
        sleep(10)
        
    def get_login_text(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/h5").text
    '''
    def click_on_directory(self):
        self.driver.find_element(By.LINK_TEXT, "Directory").click()

    def get_directory_text(self):
        return self.driver.find_element(By.LINK_TEXT, "Directory").text
    
    def find_directory_name(self):     
        return self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div").text
    
    def click_on_directory_name(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/p[1]").click()

    def get_email(self):
        parent_element = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div")
        child_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, ".com").text
        for i in parent_element:
            if i == child_element:
                return i
    '''       
    





    
