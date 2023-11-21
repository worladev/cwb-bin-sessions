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

Example Usage:

# Creating Books
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", True)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", True)

# Creating Patrons
patron1 = Patron("Alice Johnson", 1)
patron2 = Patron("Bob Smith", 2)

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
