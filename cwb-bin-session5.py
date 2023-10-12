'''
SESSION 5 (21/08/2023)
Mentor and Facilitator ==> ANDY AFFUL

PROBLEM STATEMENT: Write a function called change_case that given a string, returns a string with each upper
case letter replaced by a lower case letter and vice-versa.

'''
import string

def change_case(word):
  
  change = list() #a list variable to hold each converted character

  # return none if the word does not have alphabets alone as characters
  if not word.isalpha():
    return None

  # loop through the word and use a conditional to:
  # replace all upper case letters with lower case letters
  # replace all lower case letters with upper case letters
  for i in word:
    if i in string.ascii_lowercase:
      change.append(i.upper())
    if i in string.ascii_uppercase:
      change.append(i.lower())
    word = ''.join(change) #join all characters in the list as one string

  return word #return the changed word


# Example Cases
print(change_case("conFiDeNcE"))