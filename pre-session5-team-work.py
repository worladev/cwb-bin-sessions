'''
Password Validation Task - Code Refactoring for pre-session 4
'''
import string

invalid_password = True

#while loop to check if all requirements for the password has been met
while (invalid_password):
    #accept password from user
    password = input("Create a password of at least 8 character:")
    
    #variables to check password requirements
    lower_case = 0
    upper_case = 0
    numbers = 0
    special_characters = 0
    length_of_password = len(password)
    
    #for loop to check each character of the password entered by user.
    for char in password:
        if char in string.ascii_lowercase:
            lower_case += 1
        elif (char in string.ascii_uppercase):
            upper_case += 1
        elif (char in string.digits):
            numbers += 1
        elif (char in string.punctuation):
            special_characters += 1
        else:
            continue
    
    #check for password validity.
    if (lower_case >= 1 and upper_case >= 1 and numbers >= 1 and special_characters >= 1 and length_of_password >= 8):
        invalid_password = False
        
        #check for password strength
        if length_of_password >= 12:
            print("password is valid and very strong")
        elif length_of_password >= 10 and length_of_password < 12:
            print("password is valid and moderate")
        else:
            print("password is valid but weak")
    else:
        print("invalid password")

