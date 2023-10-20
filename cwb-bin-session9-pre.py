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
