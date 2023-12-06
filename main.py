# main.py

from library import Library

def main():
    library = Library()
    library.load_books()
    
    while True:
        print("1. Display all books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Save and exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            library.display_books()
        elif choice == "2":
            library.add_book()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.save_books()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
