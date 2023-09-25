'''
Pre Session 3 ==> Code Refactoring and Debugging
Mentor and Facilitator ==> ANDY AFFUL

WEEK 3 PRE-SESSION ASSIGNMENT (23rd July to 29th July)
You are given a function that converts a decimal number(base-10) to hexadecimal(base-16). However,
the function has several issues and could benefit from code refactoring to improve readability and
maintainability. Your task is use your knowledge from the just ended Coding Without Borders programming
class as well the example from last fix these issue.

Once you have completed the task, test the function with different inputs to ensure it produces the
expected results. Make sure to provide an explanation of the changes you made and how they address
the bugs and code quality improvements.

This task will help you practice debugging, code refactoring, and improving code quality by addressing
common issues and applying best practices.
'''
#1 Rename function
def convert_to_hex(number):

    #3 Rename variable to hold converted hexadecimal number
    converted = []
    
    #while loop to process conversion
    while number > 0:
        remainder = number % 16

        if remainder < 10:
            converted.insert(0, str(remainder))
        elif remainder == 10:
            converted.insert(0, 'A')
        elif remainder == 11:
            converted.insert(0, 'B')
        elif remainder == 12:
            converted.insert(0, 'C')
        elif remainder == 13:
            converted.insert(0, 'D')
        elif remainder == 14:
            converted.insert(0, 'E')
        else:
            converted.insert(0, 'F')

        number //= 16

    hex_num = ''.join(converted)

    return hex_num

# CASE 1
print(convert_to_hex(16))    # Output: "10"

# CASE 1
print(convert_to_hex(-10))   # Output: "-A"