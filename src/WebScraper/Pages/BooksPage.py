from src.WebScraper.BasePage import BasePage
from selenium.webdriver.common.by import By

class BooksPage(BasePage):
    BOOK_LIST = (By.XPATH, "//article[@class='product_pod']")
    TITLE = (By.TAG_NAME, "h3")
    PRICE = (By.CLASS_NAME, "price_color")
    STOCK = (By.CSS_SELECTOR, ".availability")
    RATING = (By.CSS_SELECTOR, "p.star-rating")

    def load_books(self, book_element):
        try:
            title = book_element.find_element(*self.TITLE).find_element(By.TAG_NAME, "a").get_attribute("title")
        except:
            title = "N/A"

        try:
            price = book_element.find_element(*self.PRICE).text
        except:
            price = "N/A"
        
        try:
            stock = book_element.find_element(*self.STOCK).text.strip()
        except:
            stock = "N/A"
        
        try:
            rating = book_element.find_element(*self.RATING).get_attribute("class").split()[-1]
        except:
            rating = "N/A"

        return {
            "title" : title,
            "price" : price,
            "stock" : stock,
            "rating" : rating,
        }
    
    def get_book_cards(self):
        return self.get_elements(self.BOOK_LIST)