
from selenium.webdriver.common.by import By

# в классе хранятся локаторы для страницы

class page_locators:
    locator_search_field = (By.ID, "text")
    # locator_search_button = (By.XPATH, "") - там нет кнопки
    # там еще есть другие локаторы, но мы не написали их