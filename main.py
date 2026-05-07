from storage import load_books, save_books
from services import Library
from models import Book

library = Library()
library.books = load_books("data/books.json")
while True:
    print("Список команд:")
    print("1 - Показать все книги")
    print("2 - Добавить книгу")
    print("3 - Удалить книгу")
    print("4 - Найти по названию")
    print("5 - Отметить как прочитанную")
    print("6 - Показать непрочатанные")
    print("7 - Выход")
    command = input("Введите команду: ")
    if command == "1":
        result = library.get_all_books()
        if result == []:
            print("Нет книг")
        else:
            for book in result:
                print(book)
    elif command == "2":
        try:
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год книги: "))
        except ValueError:
            print("Введён не верный год книги")
        else:
            if title.strip() != "" and author.strip() != "":
                book = Book(library.get_next_id(), title, author, year, False)
                library.add_book(book)
                save_books("data/books.json", library.books)
            else:
                print("Введено неверное название или автор")
    elif command == "3":
        try:
            ID = int(input("Введите id: "))
        except ValueError:
            print("Введён не верный id книги")
        else:
            result = library.remove_book(ID)
            if result:
                save_books("data/books.json", library.books)
                print("Удалено")
            else:
                print("Не найдено")
    elif command == "4":
        TITLE = input("Введите название книги: ")
        if TITLE.strip() != "":
            result = library.find_by_title(TITLE)
            if result == []:
                print("Нет книг")
            else:
                for book in result:
                    print(book)
        else:
            print("Введено неверное название книги")
    elif command == "5":
        try:
            ID = int(input("Введите id: "))
        except ValueError:
            print("Введён не верный id книги")
        else:
            result = library.mark_book_as_read(ID)
            if result:
                print("Отмечено")
            else:
                print("Не найдено")
            save_books("data/books.json", library.books)
    elif command == "6":
        result = library.get_unread_books()
        if result == []:
            print("Нет книг")
        else:
            for book in result:
                print(book)
    elif command == "7":
        save_books("data/books.json", library.books)
        break
    else:
        print("Введена неверная команда")
