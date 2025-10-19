import csv

OUTPUT_FILE = "/Users/aitor/Documents/Python/Selenium_Pandas/data/books.csv"

def init_csv():
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Stock", "Rating"])

def save_books_to_csv(book_info):
    with open(OUTPUT_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            book_info["title"],
            book_info["price"],
            book_info["stock"],
            book_info["rating"]
        ])

def read_csv():
    existing = set()
    try:
        with open(OUTPUT_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                key = (row['Title'].strip().lower(), row['Price'].strip().lower(), row['Stock'].strip().lower(), row['Rating'].strip().lower())
                existing.add(key)
    except FileNotFoundError:
        pass
    return existing


        