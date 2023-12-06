# library.py

import json

class Library:
    def __init__(self):
        self.books = []

    def load_books(self):
        try:
            with open("books.json", "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            pass

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book)

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        self.books.append({"title": title, "author": author})
        print("Book added successfully.")

    def borrow_book(self):
        title = input("Enter the title of the book to borrow: ")
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"{title} borrowed successfully.")
                return
        print(f"Book with title {title} not found.")

    def return_book(self):
        title = input("Enter the title of the book to return: ")
        author = input("Enter the author of the book: ")
        self.books.append({"title": title, "author": author})
        print(f"{title} returned successfully.")

    def save_books(self):
        with open("books.json", "w") as file:
            json.dump(self.books, file)
