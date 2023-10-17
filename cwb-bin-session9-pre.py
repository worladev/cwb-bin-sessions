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
