from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, setup): #konstruktor 
        self.driver = setup
    # definujeme proměnné - kdyby se někdy v budoucnu ID nebo NAME změnilo na třeba "username2", my bychom změnili pouze v proměnné
    # tzn nemusíme měnit na různých místech kódu, jen v PROMĚNNÉ

    username_name = "username"  #pozor na odsazení, atribut patří třídě LoginPage
    password_name = "password"
    login_button_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    page_title_class = "oxd-topbar-header-breadcrumb"

    #definujeme si metody, které budeme používat na přihlašovací stránce
    def input_username(self, username): 
        self.driver.find_element(By.NAME, self.username_name).clear() #vymazává znaky (kdyby tam náhodou něco bylo)
        self.driver.find_element(By.NAME, self.username_name).send_keys(username) #send_keys už voláme jako parametr metody input_username 

    def input_password(self, password):
        self.driver.find_element(By.NAME, self.password_name).clear()
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def click_on_login(self): #parametr nemusíme používat, protože to jenom kliká
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def get_title_text(self):
        return self.driver.find_element(By.CLASS_NAME, self.page_title_class).text #chceme aby nám metoda přímo vrátila text (return)
