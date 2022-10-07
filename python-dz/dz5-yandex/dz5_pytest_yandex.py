from selenium.webdriver.support import wait
from selenium import webdriver
from selenium.webdriver.common.by import By


# Задание:
# Дописать функция по нажатию на кнопку клавиатуры на ya.ru
# А также написать тест по использованию этой кнопки




# храню классы по домашке в одном файле, чтобы было удобнее смотреть

class Element():
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def click_element(self):
        element = self.driver.find_element(self.locator[0], self.locator[1])
        element.click()

    def send_key(self, word):
        element = self.driver.find_element(self.locator[0], self.locator[1])
        element.click()
        element.send_keys(word)


class Locators:
    search_field = (By.ID, "text")
    search_button = (By.CLASS_NAME, "search3__button.mini-suggest__button")
    cancel_button = (By.CLASS_NAME, "search3__svg_clear")
    element_nav_bar = (By.CLASS_NAME, "service__name")
    # добавлены новые локаторы:
    virtual_keyboard_button = (By.CLASS_NAME, "search3__svg_keyboard")



class BasePage:
    def __init__(self, base_url="https://ya.ru/"):
        self.driver = webdriver.Chrome(r"C:\Users\79521\PycharmProjects\pyProject-selenium\POM\ScyllaCloud\chromedriver.exe")
        self.base_url = base_url

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def quit_from_browser(self):
        return self.driver.quit()

    def get_driver(self):
        return self.driver


class YandexSearcher(BasePage):
    def enter_word(self, word):
        search_field = Element(self.get_driver(), Locators.search_field)
        search_field.click_element()
        search_field.send_key(word)
        return search_field


    def click_on_the_search_button(self):
        search_button = Element(self.get_driver(), Locators.search_button)
        search_button.click_element()
        return search_button

    def click_on_cancel_button(self):
        cancel_button = Element(Locators.cancel_button)
        cancel_button.click_element()
        return cancel_button

    def find_element_in_nav_bar(self):
        list_elements = self.driver.find_elements(Locators.element_nav_bar[0], Locators.element_nav_bar[1])
        return list_elements

    def click_on_the_virt_keyboard_button(self): # добавлен новый метод
        search_field = Element(self.get_driver(), Locators.search_field)
        search_field.click_element()
        virtual_keyboard_button = Element(self.get_driver(), Locators.virtual_keyboard_button)
        virtual_keyboard_button.click_element()
        return virtual_keyboard_button

