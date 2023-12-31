'''
HOLIDAY SESSION PRE-SESSION 9 (04/09/2023)
Mentor and Facilitator ==> ANDY AFFUL

TASK: IMPROVING ONLINE RESEACH SKILLS


1. FIZZBUZZ
Find a code snippet that solves the classic FizzBuzz problem, which prints numbers from 1 to 100 but replaces
multiples of 3 with "Fizz" and multiples of 5 with "Buzz."

REF: https://gist.github.com/jaysonrowe/1592775
'''
def fizzbuzz(n):
    if n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

print("\n".join(fizzbuzz(n) for n in range(1, 21)))


'''
2. PALINDROME CHECKER

Search for code that checks whether a given string is a palindrome (reads the same forwards and backwards).

REF: https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
'''
#1
def isPalindrome(s):
    return s == s[::-1]
#2
def isPalindrome(s):
    if s == s[::-1]:
      return True

#3
def palindromes(word):
  if word == word[::-1]:
    print(word, " is palindrome.")

palindromes("madam")


'''
3. FACTORIAL CALCULATOR

Find code that calculates the factorial of a given number.

REF: https://www.programiz.com/python-programming/examples/factorial
'''
#Using loops
# Python program to find the factorial of a number provided by the user.

def calculateFactorial(num):
  factorial = 1
  #check if the number is negative, positive or zero
  if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
  elif num == 0:
    print("The factorial of 0 is 1")
  else:
    for i in range(1, num + 1):
       factorial = factorial * i
  return factorial


print(f"The factorial of 7 is {calculateFactorial(7)}")


'''
4. REVERSE A STRING

Discover code that reverses the characters in a string.

REF: https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
'''
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)

print("The reversed string(using recursion) is : ", end="")
print(reverse(s))


'''
5. PRIME NUMBER CHECKER

Locate code that checks if a given number is prime.

REF: https://www.sanfoundry.com/python-program-check-prime-number/
'''
#refactore using binary search logic
#loop through the square root of n
def isPrime(n):
  k = 0
  for i in range(2, n // 2):
    if(n % i == 0):
        k = k + 1
  if(k <= 0):
    return True
  else:
    return False

isPrime(13)


'''
6. LINEAR SEARCH

Find code for a linear search algorithm that searches for a specific element in an array.

REF: https://www.geeksforgeeks.org/python-program-for-linear-search/
'''
# Searching an element in a list/array in python
# can be simply done using \'in\' operator
# Example:
# if x in arr:
# print arr.index(x)

# If you want to implement Linear Search in python

# Linearly search x in arr[]
# If x is present then return its location
# else return -1

def search(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i
	return -1


'''
7. BUBBLE SORT

Find code for the bubble sort algorithm that sorts an array of integers.

REF: https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
'''
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array
  

'''
8. CALCULATOR APP

Discover code for a simple calculator application that can perform basic operations like addition, subtraction, multiplication, and division.

REF: https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3
'''
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()


'''
9. TODO LIST APP:
Find code for a to-do list application that allows users to add, remove, and mark tasks as completed.

REF: N/A
'''
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def remove_task(self, task):
        for t in self.tasks:
            if t['task'] == task:
                self.tasks.remove(t)
                break

    def mark_task_completed(self, task):
        for t in self.tasks:
            if t['task'] == task:
                t['completed'] = True
                break

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task['completed'] else "Not Done"
                print(f"{index}. {task['task']} - Status: {status}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            task = input("Enter the task to mark as completed: ")
            todo_list.mark_task_completed(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


'''
10. NUMBER GUESSING GAME

Find code for a number guessing game where the program generates a random number, and the user tries to guess it.

REF: https://djangocentral.com/creating-a-guessing-game-in-python/
'''
import random

def number_guessing_game():
    number = random.randint(1, 10)
    
    #solving using binary search algorithm.
    # lower = 0 #
    # upper = len(number) - 1 #

    player_name = input("Hello, What's your name? ")
    number_of_guesses = 0

    print("Okay, " + player_name + "! I am guessing a number between 1 and 10:")

    while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1

        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            break

    if guess == number:
        print('Congratulations, ' + player_name + '! You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('Sorry, ' + player_name + ', you did not guess the number. The number was ' + str(number))
        

'''
11. PASSWORD GENERATOR

Discover code for a password generator that generates strong and secure passwords.

REF: https://geekflare.com/password-generator-python-code/
'''
import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# fix password length
pwd_length = 12

# generate a password string
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

# print(pwd)

# generate password meeting constraints
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in pwd) and
      sum(char in digits for char in pwd)>=2):
          break
# print(pwd)


'''
12. COUNTDOWN TIMER

Find code for a countdown timer that counts down from a specified time.

REF: https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
'''
# import the time module
import time

# define the countdown func.
def countdown(t):

	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1

	print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))


'''
13. CURRENCY CONVERTER

Locate code for a currency converter that converts between different currencies using exchange rates.

REF: https://www.learningmilestone.com/post/currency-converter-python
'''
#  According to the problem,the function display_menu should not return any value.It should just display the menu
def display_menu():
  print("1. Convert USD to Euro(EUR)")
  print("2. Convert USD to British Pound Sterling (GBP)")
  print("3. Convert USD to Japenese Yen(JPY)")
  print("4. Convert USD to Canadian Dollar(CAD)")
  print("5. Exit")
#The other four functions that convert currencies accept a value through an argument and return the converted value
def USD_to_EU(value):
  return value*0.94
def USD_to_GBP(value):
  return value*0.79
def USD_to_JPY(value):
  return value*113
def USD_to_CAD(value):
  return value*1.33
while True:
  display_menu()
  choice=int(input())
  if choice==5:
    print("Bye!")
    break
  else:
    amount=float(input("Enter an amount in US dollars: "))
    if choice==1:
      print(amount,"USD",USD_to_EU(amount),"Euro")
    elif choice==2:
      print(amount,"USD",USD_to_GBP(amount),"GBP")
    elif choice==3:
      print(amount,"USD",USD_to_JPY(amount),"JPY")
    elif choice==4:
      print(amount,"USD",USD_to_CAD(amount),"CAD")


'''
14. POWER OF TWO

Find code that determines if a number is a power of 2.

REF: geeksforgeeks.org/program-to-find-whether-a-given-number-is-power-of-2/
'''
# Python program to check if given
# number is power of 2 or not

# Function to check if x is power of 2
def isPowerOfTwo(n):
	if (n == 0):
		return False
	while (n != 1):
		if (n % 2 != 0):
			return False
		n = n // 2

	return True
#n -> n &  (n -1) > 0

# Driver code
if __name__ == "__main__":

	# Function call
	if(isPowerOfTwo(31)):
		print('Yes')
	else:
		print('No')
	if(isPowerOfTwo(64)):
		print('Yes')
	else:
		print('No')

# This code is contributed by Danish Raza


'''
15. DESIGN A BANK

Search for a code that simulates a bank handling transactions: deposit, withdraw and transfer

REF: https://www.codevscolor.com/python-bank-account-class
'''
#Multi threading applications
class Bank:
	def __init__(self):
		self.total_amount = 0
		self.name = ''

	def welcome(self):
		self.name = input('Welcome to your Bank Account. Please Enter your name: ')

	def print_current_balance(self):
		print('Your Current balance : {}'.format(self.total_amount))

	def deposit(self):
		self.total_amount += float(input('Hello {}, please enter amount to deposit: '.format(self.name)))
		self.print_current_balance()

	def withdraw(self):
		amount_to_withdraw = float(input('Enter amount to withdraw: '))

		if amount_to_withdraw > self.total_amount:
			print('Insufficient Balance !!')
		else:
			self.total_amount -= amount_to_withdraw

		self.print_current_balance()


if __name__=="__main__":
	bank = Bank()
	bank.welcome()

	while True:
		input_value = int(input('Enter 1 to see your balance,\n2 to deposit\n3 to withdraw\n'))

		if input_value == 1:
			bank.print_current_balance()
		elif input_value == 2:
			bank.deposit()
		elif input_value == 3:
			bank.withdraw()
		else:
			print('Please enter a valid input.')


#THIS IS THE LAST TASK IN THE RESEARCH SKILLS SESSION.