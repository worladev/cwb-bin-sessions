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