import pytest
from WebDriverSetup.WebDriver import init_driver
from WebScraper.Pages.HomePage import HomePage
from WebScraper.Pages.BooksPage import BooksPage

@pytest.fixture(scope="module")
def driver():
    driver = init_driver(headless=True)
    yield driver
    driver.quit()

def test_get_first_book(driver):
    homepage = HomePage(driver)
    bookspage = BooksPage(driver)
    
    homepage.open()
    
    books = bookspage.get_book_cards()
    
    assert len(books) > 0  # Debe encontrar al menos un libro

    first_book = books[0]
    book_info = bookspage.load_books(first_book)
    
    # Comprobamos que el título y precio no estén vacíos
    assert book_info["title"] != ""
    assert book_info["price"] != ""