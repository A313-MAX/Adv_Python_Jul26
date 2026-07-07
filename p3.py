# Dunder Methods : Double Underscore

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Dunder Method for String Representation for users 
    def __str__(self):
        return f"Book('{self.title}', '{self.author}"

    # Dunder Method for String Representation for developers 
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"
    
    #Equality Comparison 
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author
    

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("Python Programming", "John Zelle")
book3 = Book("Java Programming", "Daniel Liang")

# print(book1)

print(repr(book1))