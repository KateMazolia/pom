from DZ.dz_6_pom.Pages.Sign_in import Locators
from DZ.dz_6_pom.Pages.Sign_in import SignIn
from DZ.dz_6_pom.Pages.Sign_in import Element, InputElement, ButtonElement
from DZ.dz_6_pom.browser import Browser
import time
import pytest
from selenium import webdriver

# Задание: Реализовать sanity test для страницы signIn


@pytest.fixture()
def browser():
    return Browser()

def test_signin_input(browser):
    base_url = "https://cloud.scylladb.com/user/signin"
    Browser(base_url).go_to_the_page()
    signin_page = SignIn(Browser)
    signin_page.click_on_email_field()
    signin_page.email.enter_text("steir@list.ru")
    time.sleep(2)
    signin_page.click_on_password_field()
    signin_page.password.enter_text("Ma532_of$sa")
    time.sleep(2)
    signin_page.click_on_signin_button()
    time.sleep(2)
