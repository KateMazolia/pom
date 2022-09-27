import pytest
from Pages.yandex.init import Yandex_searcher
import time

def test_yandex_search():
    yandex_page = Yandex_searcher()
    yandex_page.go_to_the_site()
    yandex_page.enter_word("корова")
    yandex_page.click_on_the_search_button()
    time.sleep(3)
    yandex_page.close_browser()
