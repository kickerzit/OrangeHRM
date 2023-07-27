from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
#from time import sleep
from selenium.webdriver.common.by import By
import pytest
#from PageObjects.LoginPage import LoginPage

#inicializace driveru
@pytest.fixture
def setup():

    global driver #proměnnou určíme jako globální a múžou k ní přistupovat všechny metody
    options = Options() #mohu zavolat s nejakymi argumenty
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #inicializace Chromedriveru
    driver.implicitly_wait(10)

    driver.get("https://opensource-demo.orangehrmlive.com/") 

    return driver #vrací driver

@pytest.fixture
def setup_with_login(): #používáme v product_test.py
    global driver #proměnnou určíme jako globální a múžou k ní přistupovat všechny metody
    options = Options() #mohu zavolat s nejakymi argumenty
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #inicializace Chromedriveru
    driver.implicitly_wait(10)

    driver.get("https://opensource-demo.orangehrmlive.com/") 

    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("marek.janik")
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys("qwertz.123")
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

    return driver #vrací driver