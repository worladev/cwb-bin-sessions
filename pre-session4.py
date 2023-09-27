'''
Pre Session 3 ==> CONNECTIVES AND LOOPS
Mentor and Facilitator ==> ANDY AFFUL

WEEK 4 PRE-SESSION ASSIGNMENT (30th July to 5th August)

Scenario 1: Weekend Plans
Write a Python program that takes two inputs from the user:
"Is it Saturday?" (sat) and "Is it Sunday?" (sun). If either of these inputs is
true, the program should display "Let's have fun!" Otherwise, it should display
"Weekdays are for work."
'''
#receive first input and check if it is 'yes' or 'no'
sat = input("Is it Saturday? (enter yes/no): ")
if sat == 'yes':
    it_is_sat = True
else:
    it_is_sat = False
    
#receive second input and check if it is 'yes' or 'no'
sun = input("Is it Sunday? (enter yes/no): ")
if sun == 'yes':
    it_is_sun = True
else:
    it_is_sun = False

#display message based on input received
if it_is_sat or it_is_sun:
    print("Let's have fun!")
else:
    print("Weekdays are for work.")


