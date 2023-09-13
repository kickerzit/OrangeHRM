import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.LoginPage import LoginPage
from PageObjects.ProductPage import ProductPage

@pytest.fixture(scope="function")
def driver():

    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    options.add_argument("start-maximized")
    options.add_argument("start-fullscreen")

    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver):

    return LoginPage(driver)