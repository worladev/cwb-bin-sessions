'''
SESSION 4 IN SESSION CODING CHALLENGE(16/08/2023)
Mentor and Facilitator ==> ANDY AFFUL

Title: Duplicate Letter Detector

PROBLEM STATEMENT: You are developing a spelling checker application that needs to identify the first letter
in a given word that appears twice. Your task is to write a Python function that takes a string containing
lowercase English letters and returns the first letter that appears twice in the word.

INSTRUCTION: Implement a Python function find_first_duplicate(s) that takes the following argument:

s: A string consisting of lowercase English letters.
The function should return the first letter that appears twice in the string s. If no letter appears twice,
return None.
'''
def find_first_duplicate(string):
   dupes = set() #variable to hold characters

   #loop to add characters to dupes and return first duplicate
   for character in string:
     if character in dupes:
        return character
     else:
        dupes.add(character)

   return None #return None if there are no duplicate letters



