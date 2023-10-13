'''
SESSION 6 (23/08/2023)
Mentor and Facilitator ==> ANDY AFFUL

IN SESSIOIN (6) ENOCH'S CODING PROBLEM ANALYSIS
===============================================
PROBLEM STATEMENT: The digital root of a number n is obtained as follows: Add up the digits n to get a new
number. Add up the digits of that to get another new number.
Keep doing this until you get a number that has only one digit. That number is the digital root.For example,
if n = 45893, we add up the digits to get 4+5+8+9+3 = 29. We then add up the digits of 29 to get 2+9=11.
We then add up the digits of 11 to get 1+1=2.
Since 2 Has only one digit, 2 is our digital root. Write a function that returns the digital root of an
integer n.

'''
def digital_root(number):

     #looping for 'number' to be a single digit
     while number >= 10:
        # 'temp_number' will hold the sum of the digits of current 'number'
        temp_number = 0
        number_copy = number

        #loop to add the digits of current 'number'
        while number_copy > 0:
          #get the last digit of current 'number' and add to 'temp_number'
          temp_number += (number_copy % 10)

          #discard the last digit that was just processed
          number_copy //= 10

        #'number' is now updated to 'temp_number'
        number = temp_number # number -> 45893 -> 29 -> 11 -> 2

     return number

# Example Case
print(digital_root(45893))