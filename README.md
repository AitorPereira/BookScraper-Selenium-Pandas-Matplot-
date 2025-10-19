# 📚 Book Scraper (Selenium+Pandas+Matplot)

This repository contains a Selenium-based bot built in Python to scrape book data from [Books to Scrape](https://books.toscrape.com).  
It follows the **Page Object Model (POM)** design pattern and integrates with **Pandas** for data processing and **Matplotlib** for visualization.

---

### 🚀 Tech Stack  
• **Core:** Python 3.12+  

• **Libraries & Tools:**  
  - Selenium → browser automation  
  - Pandas → data processing and CSV handling  
  - Matplotlib → data visualization  
  - Pytest → test runner and test orchestration  
  - Unittest → WebDriver setup base  

• **Concepts Explored:**  
  - Page Object Model (POM)  
  - Automated browser interaction  
  - WebDriver setup & teardown  
  - CSV handling and data persistence  
  - Data aggregation, filtering, and plotting  

---

## 📂 Project Structure
```
src/
├── WebScraper/
│   ├── Pages/
│   │   ├── BasePage.py            # Base page object class
│   │   ├── BooksPage.py           # Book page logic and scraping
│   │   └── HomePage.py            # Home page logic, pagination
├── WebDriverSetup/
│   └── WebDriver.py               # WebDriver initialization
├── DataProcessing/
│   └── CsvHandler.py              # CSV reading and writing helpers
└── tests/
└── test.py                    # Test scripts for scraping
main.py                            # Entry point for running the scraper
data/                               # Folder to store CSV output
````

### 🔑 Key Features

1. **Page Object Model (POM)**  
   - Encapsulates web elements and interactions inside `BooksPage.py` and `HomePage.py`.  
   - Makes scraping code clean, readable, and maintainable.

2. **Reusable WebDriver Setup**  
   - Centralized `WebDriver.py` handles driver initialization, maximization, and teardown.  
   - Supports headless mode for automated runs.

3. **Automated Book Scraping**  
   - Scrapes book **Title**, **Price**, **Stock**, **Rating**, and **Link**.  
   - Handles pagination to gather more books.  
   - Saves data to CSV for analysis.

4. **Data Analysis & Visualization**  
   - Uses Pandas to filter, aggregate, and calculate statistics.  
   - Visualizes price distribution, ratings, and stock availability using Matplotlib.

5. **Extensible & Configurable**  
   - Easy to add new pages or scrape additional fields.  
   - Input-driven search for dynamic scraping.  
   - Designed to scale beyond the initial 20 books.

---

### ⚡ Getting Started

1. Clone the Repo
```bash
git clone https://github.com/YourUsername/Selenium_Books_Scraper.git
cd Selenium_Books_Scraper
```
2. Create Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
_(Make sure to include selenium, pandas, matplotlib in requirements.txt.)_

4.	Run the Scraper
```bash
python3 main.py
```
5.	Explore Data
- The scraped CSV will be saved in /data/books.csv.
- Use Pandas and Matplotlib to analyze and visualize.

### 🖥️ Example Usage
```
from src.WebScraper.Pages.HomePage import HomePage
from src.WebScraper.Pages.BooksPage import BooksPage
from src.WebDriverSetup.WebDriver import init_driver
from src.DataProcessing.CsvHandler import init_csv, save_books_to_csv

driver = init_driver(headless=True)
homepage = HomePage(driver)
books_page = BooksPage(driver)

homepage.open()
init_csv()

book_cards = books_page.get_book_cards()
for book in book_cards:
    info = books_page.load_books(book)
    save_books_to_csv(info)
driver.quit()
```

### 💡 Why this project?

✔️ Clean separation of concerns using Page Object Model.
✔️ Easy to extend and maintain scraping logic.
✔️ Combines automation with data analysis and visualization.
✔️ Great practice for beginner-to-intermediate Python developers.

### 📜 License

This project is licensed under the MIT License.

✨ Feel free to fork, contribute, or adapt this framework for your own scraping and data projects. 🚀
