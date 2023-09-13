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
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver):

    return LoginPage(driver)

@pytest.fixture(scope="function")
def logged_in_driver(login_page):

    login_page.go_to_login_page()
    login_page.input_username("standard_user")
    login_page.input_password("secret_sauce")
    login_page.click_on_login()

    yield login_page.driver

    login_page.driver.quit()

@pytest.fixture(scope="function")
def product_page(logged_in_driver):

    return ProductPage(logged_in_driver)