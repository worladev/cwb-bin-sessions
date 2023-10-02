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
