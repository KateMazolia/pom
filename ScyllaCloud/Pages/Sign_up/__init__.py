from POM.ScyllaCloud.browser import Browser
import time
from selenium import webdriver
from POM.ScyllaCloud.Pages.Sign_up import Locators
from POM.ScyllaCloud.browser import Browser
from POM.ScyllaCloud.Pages.conftest import User

from POM.ScyllaCloud.Pages.Sign_up.element import Element, InputElement, CheckBoxElement, ButtonElement


class SignUp():
    path = "/user/signup"

    def __init__(self, browser):
        self.not_filled_company_name_text = Element(driver=browser.get_driver(), locator=Locators.not_filled_company_name_text) # добавлен новый локатор
        self.first_name = InputElement(driver=browser.get_driver(), locator=Locators.first_name_locator)
        self.last_name = InputElement(driver=browser.get_driver(), locator=Locators.last_name_locator)
        self.email = InputElement(driver=browser.get_driver(), locator=Locators.email_locator)
        self.password = InputElement(driver=browser.get_driver(), locator=Locators.password_locator)
        self.company = InputElement(driver=browser.get_driver(), locator=Locators.company_locator)
        self.country = InputElement(driver=browser.driver, locator=Locators.company_country_locator)
        self.phone = InputElement(driver=browser.get_driver(), locator=Locators.phone_locator)
        self.agreement_check_box = CheckBoxElement(driver=browser.get_driver(),
                                                   locator=Locators.agreement_check_box_locator)
        self.signup_button = ButtonElement(driver=browser.get_driver(), locator=Locators.signup_button_locator)


    def signup(self, user: User):
        self.first_name.enter_text(user.first_name)
        self.last_name.enter_text(user.last_name)
        self.email.enter_text(user.email)
        self.password.enter_text(user.password())
        self.company.enter_text(user.company)
        self.country.enter_text(user.country)
        self.country.key_code()
        # time.sleep(2)
        self.phone.enter_text(user.phone)
        self.agreement_check_box.click_element()
        print(self.agreement_check_box.state())
    # time.sleep(2)
    # self.signup_button.click_element()

