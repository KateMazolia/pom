from POM.ScyllaCloud.Pages.Sign_up import Locators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from POM.ScyllaCloud.browser import Browser

class Element:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator #(By.ID, "id")
        self.element = self.driver.find_element(self.locator[0], self.locator[1])

    def click_on_element(self):
        self.element.click()


class InputElement(Element):
    def enter_text(self, text):
        self.click_on_element()
        self.element.send_keys(text)

    def get_text(self):
        return self.element.get_attribute("value")

class CheckBoxElement:
    pass


class ButtonElement:
    pass





class SignUP:

    def __init__(self, base_url="https://cloud.scylladb.com/", Browser):
        self.path = "user/signup"
        self.url = base_url + self.path
        self.first_name = InputElement()
        self.last_name = InputElement()
        self.email = InputElement()
        self.password = InputElement()
        self.company = InputElement()
        self.phone = InputElement()
        self.agreement_check_box = CheckBoxElement()
        self.signup_button = ButtonElement()

    def sign_up(self):
        pass