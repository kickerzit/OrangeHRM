from pytest_bdd import given, when, then, scenarios
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
import pytest

scenarios("../features/login.feature") 

@pytest.fixture
def setup():

    global driver #proměnnou určíme jako globální a múžou k ní přistupovat všechny metody
    options = Options() #mohu zavolat s nejakymi argumenty
    options.add_argument("start-maximized")
    #options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #inicializace Chromedriveru
    driver.implicitly_wait(10)


    yield driver #klidně může být return
                 #yield: driver bude k dispozici po celou dobu, než ty testy proběhnou a až už nebude nic
                 #co by ten driver používal, tak proběhne quit (o řádek níže)
    driver.quit()

    @pytest.fixture
    @given("I am on the login page", target_fixture="I_am_on_login") 
                                     # 1. Parametr
                                     # píšeme zde ten text, co jsme napsali do login.feature za Given - propojení
                                     # @given: dekorátor - píšeme zde nějakou metodu, která odpovídá prvnímu řádku v login.feature 
    def I_am_on_login(setup): # metodě musíme říct, odkud ten driver vezme - proto parametr setup  
        driver = setup                           
        driver.get("https://opensource-demo.orangehrmlive.com/")                              # 2. Parametr: target fixture
                                                                                              # většinou název metody, kterou píšeme
                                                                                              # target_fixture="I_am_on_login"
    @when("I enter valid credentials")
    def enter_correct_username_and_pwd():
        driver.find_element(By.NAME, "username").clear() #vymazává znaky (kdyby tam náhodou něco bylo)
        driver.find_element(By.NAME, "username").send_keys("Admin") 

        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")

    @when("I press on the login button") # v login.feature jako And
    def click_on_login():
        
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

    @then("I see that I am logged in")
    def verify_ok_login():
        title_text = driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb").text
        if title_text == "Dashboard":
            assert True

        else:
            print("Test Failed!")
            assert False

    @when("I enter invalid credentials")
    def enter_incorrect_username_and_pwd():
        driver.find_element(By.NAME, "username").clear() #vymazává znaky (kdyby tam náhodou něco bylo)
        driver.find_element(By.NAME, "username").send_keys("Admi") 

        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admi123")

    @then("I see error message")
    def verify_non_ok_login():
        
        get_error_message = driver.find_element(By.CLASS_NAME, "oxd-text oxd-text--p oxd-alert-content-text").text
        
        if get_error_message == "Invalid credentials":
            assert True

        else:
            print(get_error_message)
            print("Test Failed!")
            assert False