from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from time import sleep
from selenium.webdriver.common.by import By
import pytest

# Pro Pytest platí, že metody musí mít prefix test_ => tím Pytest zjistí, které metody jsou testovací
# a vše co je test_setup, test_login... bere jako test
#inicializace driveru
@pytest.fixture
def test_setup():

    global driver #proměnnou určíme jako globální a múžou k ní přistupovat všechny metody
    options = Options() #mohu zavolat s nejakymi argumenty
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #inicializace Chromedriveru
    driver.implicitly_wait(10)

@pytest.mark.sanity
def test_login(test_setup): #když používáme marker @pytest.fixture, musíme zde definovat jako parametr test_setup
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    driver.find_element(By.NAME, "username").send_keys("Admin")
    #sleep(3)
    driver.find_element(By.NAME, "password").send_keys("admin123")
    #sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    #driver.implicitly_wait(5)   

#ověření metody test login
@pytest.mark.sanity
def test_verify_ok_login():
    title = driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb").text
    sleep(3)
    assert title == "Dashboard"
    sleep(3)

#aby po testu nezůstal žádnej bordel, nebo se pouze driver zavřel
@pytest.mark.sanity
def test_teardown():
    driver.close()
    driver.quit()
    print("Test has been done")


