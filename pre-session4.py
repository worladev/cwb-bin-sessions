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

#display message based on value of input received
if it_is_sat or it_is_sun:
    print("Let's have fun!")
else:
    print("Weekdays are for work.")


'''
Scenario 2: Ticket Purchase
Write a Python program that takes two inputs from the user:
"Is the customer a student?" (student) and "Is the customer a senior citizen?" (senior).
If the customer is a student OR a senior citizen, the program should display "You are eligible for a
discount!" Otherwise, it should display "No discount available."
'''
#accept input one and check if it is 'yes' or 'no'
customer_type = input("Is the customer a student? (enter yes/no): ")
if customer_type == 'yes':
    is_a_student = True
else:
    is_a_student = False

#accept input two and check if it is 'yes' or 'no'
customer_type2 = input("Is the customer a senior citizen? (enter yes/no): ")
if customer_type2 == 'yes':
    is_a_senior_citizen = True
else:
    is_a_senior_citizen = False

#display message based on value of input received
if is_a_student or is_a_senior_citizen:
    print("You are eligible for a discount!.")
else:
    print("No discount available.")


'''
Scenario 3: Password Verification
Write a Python program that asks the user to enter a password. If the password matches "Secret123,"
the program should display "Access granted." Otherwise, it should display "Access denied."
'''
# refactoring needed.
correct_password = "Secret123"

passw = input("Enter your password: ")
if passw == correct_password:
    print("Access granted")
else:
    print("Access denied")
# refactoring needed.


'''
Scenario 4: Temperature Classification
Write a Python program that takes the temperature as input. If the temperature is less than 0 degrees
Celsius OR greater than 30 degrees Celsius, the program should display "Extreme weather conditions.
Stay indoors." Otherwise, it should display "Enjoy the day!"
'''
#accept temperature input from user 
temp = int(input("Enter temperature: "))

#display message based on temperature input
if temp < 0 or temp > 30:
    print("Exteme weather conditions. Stay indoors.")
else:
    print("Enjoy the day!")

