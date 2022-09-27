from POM.browser import Browser
from POM.Pages.yandex.Locators import Locators


class YandexSearcher(Browser):
    def enter_word(self, word):
        search_field = self.driver.find_element(Locators.search_field[0], Locators.search_field[1])
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        search_button = self.driver.find_element(Locators.search_button[0], Locators.search_button[1])
        search_button.click()
        return search_button