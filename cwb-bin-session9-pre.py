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