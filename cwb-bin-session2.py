'''
SESSION 2 (09/08/2023)
Mentor and Facilitator ==> ANDY AFFUL

PROBLEM STATEMENT ==> Voter Registry Cleanup
During an audit of the electoral commission of the nation of Mackie, it was discovered that some people
registered more than once to vote. In the voter registry, a citizen is identified by the social security
number assigned to them from birth. The commission has been tasked to find the actual number of eligible
Mackie citizens who are eligible to vote. Your task is to write a program that, given a list of social
security numbers, can achieve this.

Additionally, the commission wants to identify the individuals who registered more than once and prosecute them,
as it is illegal to register more than once. Your task is to write a program that, given a list of social security
numbers, achieves both goals.

Input:
['123456789', '987654321', '555555555', '123456789', '111111111']

Output:
Actual number of eligible voters: 4
Voters who registered more than once: ['123456789']

- ALGORITHM
  - Create a new set variable l.
  - Create a new set variable j.
  - Loop through the input list
   - if ID in j append ID to l.
   - else add ID to j.
  - Get the number of unique ID's in j as eligible voters.
  - Display total number of eligible voters in j.
  - Display duplicate ID's in l.
  
'''
# Solution to Second Session Task

def find_eligible(id_list):
  # a set variable to hold id's to avoid duplicates
  unique_list = set()

  # a list variable to hold id's that are registered more than once.
  multiple_id = set() #---> refactored to a set type

  # a loop to check for unique id's and id's that appear more than once.
  for id in id_list:
    if id in unique_list:
      multiple_id.add(id) # add duplicate id's to multiple_id
    else:
      unique_list.add(id) # add unique id's to unique_id

  # getting the number of unique registered id's
  unique_list_length = len(unique_list)

  # a formated string containing the length of eligible and duplicate voters.
  output_string = f'''
  Actual number of eligible voters: {unique_list_length}
  Voters who registered more than once: {multiple_id}
  '''

  # return formated string
  return output_string


# CASE - empty list
ssn_list = []
print(find_eligible(ssn_list))

# CASE 1
ssn_list1 = ['123456789']
print(find_eligible(ssn_list1))

# CASE 2
ssn_list2 = ['123456789', '987654321', '555555555', '123456789', '111111111']
print(find_eligible(ssn_list2))

# CASE 3
ssn_list3 = ['123456789', '987654321', '555555555', '123456789', '111111111', '555555555', '010342433']
# print(find_eligible(ssn_list3))

