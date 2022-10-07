from DZ.dz_5_pytest.dz5_pytest_yandex import Element, Locators, BasePage, YandexSearcher
import pytest
import time


@pytest.fixture()
def yandex_page():
    return YandexSearcher()

@pytest.fixture()
def browser(yandex_page):
    yandex_page.go_to_site()
    yield
    yandex_page.quit_from_browser()

def test_virtual_keyboard_bar_is_appear(yandex_page, browser): # добавлен новый тест, проверяется, что окно клавиатуры появляется на экране
    yandex_page.click_on_the_virt_keyboard_button()
    time.sleep(2)

def test_if_virtual_keyboard_bar_closes(yandex_page, browser): # добавлен новый тест, проверяется, что окно клавиатуры закрывается при повторном нажатии
    yandex_page.click_on_the_virt_keyboard_button()
    time.sleep(2)
    yandex_page.click_on_the_virt_keyboard_button()
    time.sleep(2)



