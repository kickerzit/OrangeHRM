from pytest_bdd import given, when, then, scenarios
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from conftest import driver
from time import sleep
import pytest

scenarios("../features/login.feature") 
@pytest.fixture(scope="function")
def login_page(driver):
    
    return LoginPage(driver)
@given("I am on the login page")    
# 1. Parametr
# píšeme zde ten text, co jsme napsali do login.feature za Given - propojení
# @given: dekorátor - píšeme zde nějakou metodu, která odpovídá prvnímu řádku v login.feature 
def I_am_on_login_page(login_page):
    login_page.go_to_login_page()

@when("I enter valid credentials")
def enter_correct_username_and_pwd(login_page):
    login_page.input_username()
    login_page.input_password()

@when("I press on the login button") # v login.feature jako And
def click_on_login(login_page):
    login_page.click_on_login()

@then("I see that I am logged in")
def verify_ok_login(login_page):
    title_text = login_page.get_title_text()
    sleep(2)
    if title_text == "Dashboard":
        assert True

    else:
        print("Test Failed!")
        assert False

'''
@then("I see that I am not logged in")
def verify_non_ok_login(login_page):

    get_error_message = login_page.get_error_message()

    sleep(2)
        
    if get_error_message == "Epic sadface: Username and password do not match any user in this service":
        assert True
    
    else:
        print(get_error_message) 
        print("Test Failed!")
        assert False
'''
@when("I enter invalid credentials")
def enter_incorrect_username_and_pwd():
    login_page.input_username("wrong_user")
    login_page.input_password("wrong_password")

@then("I see error message")
def verify_non_ok_login(login_page):
    
    get_error_message = login_page.get_error_message()
    
    if get_error_message == "Invalid credentials":
        assert True

    else:
        print(get_error_message)
        print("Test Failed!")
        assert False