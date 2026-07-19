class Book:

    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies = self.available_copies - 1
            print("Book borrowed successfully.")
        else:
            print("No copies available.")

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies = self.available_copies + 1
            print("Book returned successfully.")
        else:
            print("All copies are already in the library.")

    def display_details(self):
        print("\nBook ID :", self.book_id)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Available Copies :", str(self.available_copies) + "/" + str(self.total_copies))


# Taking input from the user
book_id = int(input("Enter Book ID: "))
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
total_copies = int(input("Enter Total Copies: "))

# Creating object
book1 = Book(book_id, title, author, total_copies)

# 1. Display details
book1.display_details()

# 2. Borrow twice
book1.borrow_book()
book1.borrow_book()

# 3. Display details
book1.display_details()

# 4. Borrow twice
book1.borrow_book()
book1.borrow_book()

# 5. Return once
book1.return_book()

# 6. Display details
book1.display_details()