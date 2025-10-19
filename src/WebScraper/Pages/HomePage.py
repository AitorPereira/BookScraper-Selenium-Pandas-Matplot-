from selenium.webdriver.common.by import By
from WebScraper.BasePage import BasePage

class HomePage(BasePage):
    URL = "https://books.toscrape.com/"
    NEXT_PAGE = (By.XPATH, "//li[@class='next']/a")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.URL)

    def go_to_next_page(self):
        if self.exists(self.NEXT_PAGE, timeout=5):
            self.click(self.NEXT_PAGE)
            return True
        return False