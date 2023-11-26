'''
NOT AVAILABLE SESSION 21 (18/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Implementing a Library Catalog

PROBLEM STATEMENT: Imagine you are developing a Library Catalog system, a management software for a local
community library. This system will help librarians track available books, manage patrons, and monitor book
borrowing and return activities. Implement the following classes:

Book:
•	Properties: Title, Author, ISBN, Availability (boolean indicating if the book is available for borrowing)
•	Methods: __init__() for initialization, get_details() to return book details.
Patron:
•	Properties: Name, Patron ID, Number of books currently borrowed
•	Methods: __init__() for initialization, get_details() to return patron details.
LibraryCatalog:
•	Properties: List of books, List of patrons, Dictionary to track borrowing transactions
    (Patron ID as key and list of borrowed books as value)
•	Methods:
1.	add_book(book: Book) to add a book to the catalog.
2.	remove_book(isbn: str) to remove a book from the catalog based on ISBN.
3.	add_patron(patron: Patron) to add a patron to the library system.
4.	remove_patron(patron_id: int) to remove a patron from the system based on Patron ID.
5.	borrow_book(patron_id: int, isbn: str) to allow a patron to borrow a book. Update book availability and
    patron's borrowed books.
6.	return_book(patron_id: int, isbn: str) to allow a patron to return a book. Update book availability and
    patron's borrowed books.
7.	get_borrowed_books(patron_id: int) to return a list of books currently borrowed by a patron.


# Creating Library Catalog
library = LibraryCatalog()
library.add_book(book1)
library.add_book(book2)
library.add_patron(patron1)
library.add_patron(patron2)

# Borrowing and Returning Books
library.borrow_book(1, "9780316769488")
library.borrow_book(2, "9780061120084")
library.return_book(1, "9780316769488")

# Retrieving Patron's Borrowed Books
print(library.get_borrowed_books(1))  # Output: ["To Kill a Mockingbird"]
print(library.get_borrowed_books(2))  # Output: []

NOTE
LibraryCatalog class allows librarians to manage books and patrons efficiently. Books can be borrowed and
returned, and librarians can track which books are currently borrowed by each patron
'''
# Book Class
class Book:
    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available
    # a function to return the attributes of the Book class
    def get_details(self):
        return [self.title, self.author, self.isbn, self.is_available]
    # a helper function to present the attributes in a string format
    def __str__(self):
        return f"{[self.title, self.author, self.isbn, self.is_available]}"

# Patron Class
class Patron:
    def __init__(self, name, id, no_of_books_borrowed = 0):
        self.name = name
        self.id = id
        self.no_of_books_borrowed = no_of_books_borrowed
    # a function to return the attributes of the Patron class
    def get_details(self):
        return [self.name, self.id, self.no_of_books_borrowed]
    # a helper function to present the attributes in a string format
    def __str__(self):
        return f"{[self.name, self.id, self.no_of_books_borrowed]}"
    

class LibraryCatalog():
    def __init__(self):
        self.transactions = dict()
        self.catalog = list()
        self.patrons = list()
    
    # a function to add a book to the catalog.
    def add_book(self, book:Book):
        if isinstance(book, Book): #check if the book passed as argumment is a valid instance of the Book class
            self.catalog.append(book)
        else:
            print("Invalid Book")
    
    # a function to remove a book from the catalog based on ISBN.
    def remove_book(self, isbn):
        for book in self.catalog:
            if book.isbn == isbn: #check if a book in the catalog have the same isbn number as the book passed as argument
                self.catalog.remove(book)
        


# Example Usage:
# Creating Book instances
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", True)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", True)


# Creating Patron instances
patron1 = Patron("Alice Johnson", 1)
patron2 = Patron("Bob Smith", 2)


# Creating Library Catalog
library = LibraryCatalog()
library.add_book(book1)
library.add_book(book2)

