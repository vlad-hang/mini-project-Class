import json
from models import Book
def load_books(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            result = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    else:
        books = []
        for book in result:
            obj = Book(
                book["id"],
                book["title"],
                book["author"],
                book["year"],
                book["is_read"]
            )
            books.append(obj)
        return books
def save_books(file_path, books):
    data = []
    for book in books:
        data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "is_read": book.is_read
        })
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)