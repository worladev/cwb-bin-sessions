'''
SESSION 6 (23/08/2023)
Mentor and Facilitator ==> ANDY AFFUL


TITLE: "Guess the Page Number Game"

PROBLEM STATEMENT: You are a teacher who has hidden a clue to a test within a 700-page book. Your goal is to create a fun game for your students to
see who can guess the correct page number containing the clue in the shortest possible time.

INSTRUCTION: Implement a Python function guess_the_page(book_pages) that takes the following argument:
book_pages: The total number of pages in the book (in this case, 700 pages).

Inside the guess_the_page function, generate a random integer between 1 and book_pages (inclusive) as the
target page number containing the clue. Prompt the player (student) to enter their guess for the page number.
Provide feedback on whether the guess is too high, too low, or correct. Continue prompting the player for
guesses until they correctly guess the page number containing the clue. Keep track of the number of guesses
it takes the player to find the correct page. Once the player correctly guesses the page number, display a
message indicating the number of attempts it took to guess correctly.
'''