import pytest
from POM.ScyllaCloud.Pages.Sign_up import SignUp
from POM.ScyllaCloud.browser import Browser
import time
import string
from POM.ScyllaCloud.Pages import conftest
from selenium import webdriver

@pytest.fixture()
def browser():
    return Browser()

class TestSignUpPage:

    def test_signup(self, browser, user_test):
        browser.go_to_site(SignUp.path)
        browser.driver.implicitly_wait(5)
        page = SignUp(browser)
        page.signup(user=user_test)
        print(page.email.get_text())
        time.sleep(2)
        #assert browser.current_url == base_url + "/"

# ДЗ: Реализовать один любой тест для страницы sigUp (кроме sаnity тест, то что реализовано на уроке)

    def test_invalid_company_name_message_show_up(self, browser):
        browser.go_to_site(SignUp.path)
        page = SignUp(browser)
        page.not_filled_company_name_text.click_element()
        page.company.enter_text("B")
        time.sleep(2)
        if page.not_filled_company_name_text.text == "Please enter a valid company name":
            page.company.enter_text("oba")
            time.sleep(2)










# class Test_sign_up_page: - старый вариант, без конфтеста
#     def test_signup(self, browser):
#         base_url = "https://cloud.scylladb.com"
#         Browser(base_url).go_to_the_page()
#         page = SignUp(Browser)
#         page.first_name.enter_text("Ivan")
#         page.last_name.enter_text("Ivanchenko")
#         page.email.enter_text("steir@list.ru")
#         page.password.enter_text("1264naM_52") # минимум 8 символов, 1 спецсимвол, 1 большая буква, 1 цифра
#         page.company.enter_text("Biba")
#         page.country.enter_text("Brasil")
#         page.phone.enter_text("88005553535")
#         time.sleep(3)
#         page.agreement_check_box.click_on_element()
#         page.signup_button.click_on_element()


