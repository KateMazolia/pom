import pytest
from  selenium import webdriver

# здесь указывается каким браузером будут открываться тесты. фикстура, потому что это значение будет передаваться много раз

@pytest.fixture(scope="session") #важно указать сессию, чтобы оно один раз запускалось, а не много
def browser():
    driver = webdriver.Chrome(executable_path=r"C:\Users\79521\PycharmProjects\pyProject-selenium\POM-lessons-autotesting\chromedriver.exe")
    yield driver
    driver.quit() #выйдется из драйвера в конце сессии

class base_page(): #класс для того, чтобы браузер дождался загрузки элементов страницы
    def __init__(self, driver, base_url="https://ya.ru"):
        self.driver = driver
        self.base_url = base_url

    # def find_element(self): функция - найти элемент и его дождаться

    def go_to_the_site(self): # метод перехода на сам сайт
        return self.driver.get(self.base_url)
