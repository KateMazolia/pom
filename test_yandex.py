import pytest
from Pages.yandex.init import YandexSearcher
from POM.Pages.yandex.Locators import Locators
import time

@pytest.fixture()
def yandex_page():
    return YandexSearcher() #возвращает класс, чтобы можно было к нему обратиться

@pytest.fixture()
def browser(yandex_page):
    yandex_page.go_to_the_site()
    yield
    yandex_page.close_browser()

def test_enter_and_clear_the_search_field(yandex_page, browser):
    yandex_page.enter_word("кот")
    yandex_page.click_on_the_search_button()
    time.sleep(3)

def test_search(yandex_page, browser):
    yandex_page.enter_word("корова")
    time.sleep(2)
    yandex_page.click_on_cancel_input_button()
    yandex_page.enter_word("кот")
    time.sleep(1)
    yandex_page.click_on_the_search_button()
    time.sleep(2)



def test_check_finding_elems_in_nav_bar(yandex_page, browser):
    yandex_page.enter_word("кот")
    yandex_page.click_on_the_search_button()
    time.sleep(2)
    elements = yandex_page.find_element_in_nav_bar()
    for elem in elements:
        elem.click()
        time.sleep(2)
        #здесь надо прописать, чтобы браузер возвращался назад, чтобы второй элемент так же кликнулся




# # если без фикстур это делать:
# # заходит на страницу, набирает в поиске "кот", нажимает найти, выходит из браузера
# def test_enter_and_clear_the_search_field():
#     yandex_page = YandexSearcher()
#     yandex_page.go_to_the_site()
#     yandex_page.enter_word("кот")
#     time.sleep(1)
#     yandex_page.click_on_the_search_button()
#     time.sleep(3)
#     yandex_page.close_browser()
#
#
# # заходит на сайт ya.ru, вводит слово "корова", отменяет ввод, вводит слово "кот", нажимает найти и затем выходит из браузера
# def test_search():
#     yandex_page = YandexSearcher()
#     yandex_page.go_to_the_site()
#     yandex_page.enter_word("корова")
#     time.sleep(2)
#     yandex_page.click_on_cancel_input_button()
#     yandex_page.enter_word("кот")
#     time.sleep(1)
#     yandex_page.click_on_the_search_button()
#     time.sleep(2)
#     yandex_page.close_browser()
