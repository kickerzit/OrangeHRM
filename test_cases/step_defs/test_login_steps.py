from pytest_bdd import given, when, then, scenarios
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import driver
from PageObjects.LoginPage import LoginPage
from time import sleep

scenarios("../features/login.feature")

@pytest.fixture(scope='function')
def login_page(driver):
    
    return LoginPage(driver)

@given("I am on the Login Page")
def I_am_on_login_page(login_page):

    login_page.go_to_login_page()

@when("I enter correct username and password")
def enter_correct_username_and_password(login_page):

    login_page.input_username("standard_user")
    login_page.input_password("secret_sauce")

@when("I enter incorrect username and password")
def enter_correct_username_and_password(login_page):

    login_page.input_username("wrong_user")
    login_page.input_password("wrong_password")
    
@when("I click on Login button")
def click_on_login(login_page):

    login_page.click_on_login()

@then("I see that I am logged in")
def verify_ok_login(login_page):

    title_text = login_page.get_title_text()

    sleep(2)

    if title_text == "Products":
        assert True
    
    else: 
        print("Test Failed!")
        assert False
    
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