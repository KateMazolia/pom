# в классе хранятся локаторы для страницы

from selenium.webdriver.common.by import By


class Locators:
    search_field = (By.ID, "text")
    search_button = (By.CLASS_NAME, "search3__button mini-suggest__button")
    cancel_input_button = (By.CLASS_NAME, "search3__svg_clear")

