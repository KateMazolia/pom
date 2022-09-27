# from POM-lessons-autotesting import browser-info если бы эта байда работала, не пришлось бы копировать описание класса браузер из browser-info

class base_page(): #класс для того, чтобы браузер дождался загрузки элементов страницы
    def __init__(self, driver, base_url="https://ya.ru"):
        self.driver = driver
        self.base_url = base_url

    # def find_element(self): функция - найти элемент и его дождаться

    def go_to_the_site(self): # метод перехода на сам сайт
        return self.driver.get(self.base_url)

import Locators

class Searcher(base_page):
    # атрибут поисковой строки
    # метод, который кликает на поисковую строку
    # метод, который вводит слова в поисковую строку
    # метод, который нажимает энтер на клавиатуре


