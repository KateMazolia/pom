from DZ.dz_6_pom.browser import Browser
from DZ.dz_6_pom.Pages.Sign_in import Locators
from DZ.dz_6_pom.Pages.Sign_in.Elements import Element, InputElement, ButtonElement
from selenium import webdriver


class SignIn(Browser):
    def __init__(self, browser):
        super().__init__()
        self.driver = webdriver.Chrome(r"C:\Users\79521\PycharmProjects\pyProject-selenium\DZ\dz_6_pom\chromedriver.exe")
        self.email = InputElement(driver=browser.get_driver(self), locator=Locators.email_locator)
        self.password = InputElement(driver=browser.get_driver(self), locator=Locators.password_locator)
        self.signin_button = ButtonElement(driver=browser.get_driver(self), locator=Locators.signin_button_locator)

    def click_on_email_field(self):
        email_field = self.driver.find_element(Locators.email_locator[0], Locators.email_locator[1])
        email_field.click()
        return email_field

    def click_on_password_field(self):
        password_field = self.driver.find_element(Locators.password_locator[0], Locators.password_locator[1])
        password_field.click()
        return password_field

    def click_on_signin_button(self):
        signin_button = self.driver.find_element(Locators.signin_button_locator[0], Locators.signin_button_locator[1])
        signin_button.click()
        return signin_button


