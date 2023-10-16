'''
SESSION 7 (28/08/2023)
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
# Code needs refactoring.

import random

def guess_the_page(book_pages):

  # check if list is empty
  if len(book_pages) == 0:
    return None

  # a random number generated between 1 and book pages
  target_page_number = random.randrange(700)

  # start search using whole list
  low = 0
  upper = len(book_pages) - 1

  count = 1  # a variable to keep count of number of guesses

  while low <= upper:
     # compute middle index and value
     mid = low + (upper - low) // 2

     if mid == target_page_number:

        # ask user to guess target value
        player_guess = int(input("Guess the page number: "))

        if player_guess == target_page_number:  # value found
           print(f"Correct!\n Total guess: {count}")
           break
        elif player_guess > target_page_number: # if user guess number is greater than target value
           print("Too High.")
        else:    # if user guess number is less than target value
           print("Too Low.")
        count += 1 # add 1 to count value

     elif mid < target_page_number:
        low = mid + 1
     elif mid > target_page_number:
        upper = mid - 1

  return target_page_number


# Test Cases
book_pages = list()  # list variable to hold number of pages in the book.
for num in range(1, 701): # a for loop to add each page number to the list variable.
   book_pages.append(num)

print(guess_the_page(book_pages))

