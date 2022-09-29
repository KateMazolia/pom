from POM.basePage import BasePage
from POM.Pages.yandex.Locators import Locators


class YandexSearcher(BasePage):
    def enter_word(self, word):
        search_field = self.driver.find_element(Locators.search_field[0], Locators.search_field[1])
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        search_button = self.driver.find_element(Locators.search_button[0], Locators.search_button[1])
        search_button.click()
        return search_button

    def click_on_cancel_input_button(self):
        cancel_input_button = self.driver.find_element(Locators.cancel_input_button[0], Locators.cancel_input_button[1])
        cancel_input_button.click()
        return cancel_input_button