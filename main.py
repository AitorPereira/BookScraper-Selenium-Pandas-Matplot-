from selenium.common.exceptions import WebDriverException, InvalidSessionIdException
from src.WebScraper.Pages.BooksPage import BooksPage
from src.WebScraper.Pages.HomePage import HomePage
from src.WebDriverSetup.WebDriver import init_driver
from src.DataProcessing.CsvHandler import *
import math

def main():
    driver = init_driver(headless=False)
    
    homepage = HomePage(driver)
    bookspage = BooksPage(driver)

    homepage.open()
    init_csv()
    
    books_saved = 0
    seen_books = set()
    page_count = 0

    try:
        print("-------------Welcome to the Book Scraper-------------")
        num_books_to_scrape = int(input("\nEnter the number of books you want to scrape: "))

        num_pages = math.ceil(num_books_to_scrape / 20)

        while books_saved < num_books_to_scrape and page_count < num_pages:

            try:
                book_cards = bookspage.get_book_cards()
                if not book_cards:
                    print("No books visible")
                
                for book in book_cards:
                    if num_books_to_scrape <= books_saved:
                        break
                    
                    try:
                        book_info = bookspage.load_books(book)
                        if not book_info or not book_info["title"]:
                            continue

                        # book_key = (
                        #     book_info["title"].strip().lower(),
                        #     book_info["price"].strip().lower(),
                        #     book_info["stock"].strip().lower(),
                        #     book_info["rating"].strip().lower(),
                        # )

                        # This is the same thing dynamically:
                        book_key = tuple(v.strip().lower() for v in book_info.values())

                        if book_key in seen_books:
                            continue
                        seen_books.add(book_key)

                        save_books_to_csv(book_info)
                        books_saved += 1
                        print(f"[{books_saved}/{num_books_to_scrape}] {book_info['title']}")

                    except (WebDriverException, InvalidSessionIdException):
                        print("Error loading books..")
                        continue

                if books_saved < num_books_to_scrape:
                    homepage.go_to_next_page()
                    page_count += 1
                else:
                    break

            except (WebDriverException, InvalidSessionIdException) as e:
                print(f"⚠️ Critical error detected: {e}")
                continue

    finally:
        driver.quit()
        print(f"Bot finished. Total books analyzed: {books_saved}")

if __name__ == "__main__":
    main()