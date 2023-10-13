'''
SESSION 6 (23/08/2023)
Mentor and Facilitator ==> ANDY AFFUL

Shared Questions Solver
PROBLEM STATEMENT: The CWB instructor gave two groups of students a list of coding questions to solve. 
our task is to write a Python program that helps you identify the questions that were solved by both groups.
Each group's list of solved questions is represented as a list of question IDs.

INSTRUCTION: Implement a Python function find_shared_questions(group1, group2) that takes the following
arguments:

group1: A list of question IDs solved by the first group of students.
group2: A list of question IDs solved by the second group of students.

The function should return a list of question IDs that were solved by both groups, representing the
intersection of the two lists. If there are no shared questions, return an empty list.

Example 1:
group1 = [1, 3, 5, 7, 9]
group2 = [2, 4, 6, 8, 10]
shared_questions = find_shared_questions(group1, group2)
print(shared_questions)  # Output: []


Example 2:
group1 = [1, 3, 5, 7, 9]
group2 = [3, 5, 8, 10, 12]
shared_questions = find_shared_questions(group1, group2)
print(shared_questions)  # Output: [3, 5]
'''