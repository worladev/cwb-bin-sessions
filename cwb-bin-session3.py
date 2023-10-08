'''
SESSION 3 (14/08/2023)
Mentor and Facilitator ==> ANDY AFFUL

Title: Custom List Counter - Implement Your Own count() Function

PROBLEM STATEMENT: As part of your journey to become proficient Python programmers, you have been given a
challenge to implement your own version of the count() function for lists.
This function should count the occurrences of a specified element in a given list, just like the built-in
count() method in Python. Your task is to write a Python function custom_count() that replicates the
behavior of the count() method.

Instructions:
Implement a Python function custom_count(lst, element) that takes a list lst and an element element as arguments and
returns the count of how many times the element appears in the list.

# Test the custom_count function
             0         1         2       3         4       5
fruits = ['apple', 'banana', 'orange', 'apple', 'grape', 'apple']
apple_count = custom_count(fruits, 'apple')
print("Number of apples:", apple_count)

numbers = ['3', '7', '2', '3', '1', '1', '3', '3', '7']
three_count = custom_count(number, '3')
print("Number of threes:", three_count)


ALGORITHM
- create a variable count initialised to 0
- loop through the list lst
- compare element of each index in lst to specified element
- if lst item is the same as element, increment count by 1 else continue
- return count value
'''
def custom_count(lst, element):

  # a variable to hold the count of the specified element
  count = 0

  # a variable to get the number of items in the list
  length = len(lst)

  # a condition to return 0 if the list is empty
  if length == 0:
    return 0

  # a loop to check through each index and determine if it contains
    # the specified element. if it does, increment count by one.
  for item in lst:
    if item == element:
      count += 1

  # return the value of count
  return count

#Test Cases
#empty list
names = []
name_count = custom_count(names, 'Confidence')
print("Number of names:", name_count)

# one item list and empty parameter for element
names2 = ['Mike']
name2_count = custom_count(names2, '')
print("Number of names:", name2_count)

# list with more items
fruits = ['apple', 'banana', 'orange', 'apple', 'grape', 'apple']
apple_count = custom_count(fruits, 'apple')
print("Number of apples:", apple_count)

# number list and an item not in the list as element parameter
numbers = ['7', '1']
five_count = custom_count(numbers, '5')
print("Number of threes:", five_count)

# number list with more items
numbers2 = ['3', '7', '2', '3', '1', '1', '3', '3', '7']
three_count = custom_count(numbers2, '3')
print("Number of threes:", three_count)