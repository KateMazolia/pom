from selenium import webdriver

class Browser:
    def __init__(self, base_url="https://cloud.scylladb.com/user/signin"):
        self.driver = webdriver.Chrome()
        self.base_url = base_url

    def go_to_the_page(self):
        return self.driver.get(self.base_url)

    def get_driver(self):
        return self.driver

    def close_browser(self):
        return self.driver.quit()
