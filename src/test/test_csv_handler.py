import os
import pytest
from DataProcessing.CsvHandler import init_csv, save_books_to_csv, OUTPUT_FILE

@pytest.fixture(autouse=True)
def setup_csv():
    # Antes de cada test, inicializa el CSV
    init_csv()
    yield
    # Después de cada test, borra el archivo
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

def test_save_books_to_csv():
    book_info = {
        "title": "Test Book",
        "price": "£10.00",
        "stock": "In stock",
        "rating": "Five"
    }
    save_books_to_csv(book_info)
    
    # Comprobamos que el archivo fue creado y contiene la fila
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Test Book" in content
        assert "£10.00" in content