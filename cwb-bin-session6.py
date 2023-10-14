'''
SESSION 6 (23/08/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: "Shared Questions Solver"

PROBLEM STATEMENT: The CWB instructor gave two groups of students a list of coding
questions to solve. Our task is to write a Python program that helps you identify the questions that were solved
by both groups. Each group's list of solved questions is represented as a list of question IDs.

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

ALGORITHM
- create list variable l to hold question IDs solved by the two groups
- create 2 set variable and cast the list into them to remove duplicated IDs
- loop through group1 list of IDs
- check if same ID is in group2 ID list
- if yes, append ID to list l
- return list l
'''
def find_shared_questions(group1, group2):
    #a list variable to hold the ID solved by both groups
    shared_questions = list()

    #a check for null or empty list from any of the group    
    if group1 is None or len(group1) <= 0:
      return shared_questions
    if group2 is None or len(group2) <= 0:
      return shared_questions

    #loop through group 1 ID list and check if same ID is in group 2s list
    # if yes, append that ID to a list
    for item in group1:
        if item in group2:
            shared_questions.append(item)

    #return the list of same IDs
    return shared_questions


# Example Case 1
group1 = [1, 3, 5, 7, 9]
group2 = [2, 4, 6, 8, 10]
shared_questions = find_shared_questions(group1, group2)
print(shared_questions)  # Output: []

# Example Case 2
group1 = [1, 3, 5, 7, 9]
group2 = [3, 5, 8, 10, 12]
shared_questions2 = find_shared_questions(group1, group2)
print(shared_questions2)  # Output: [3, 5]

# Example Case 3
group1 = []
group2 = [3, 5, 8, 10, 12]
shared_questions3 = find_shared_questions(group1, group2)
print(shared_questions3)  # Output: []

# Example Case 4
group1 = [1, 3, 5, 7, 8, 9]
group2 = [3, 5, 8, 10, 12]
shared_questions4 = find_shared_questions(group1, group2)
print(shared_questions4)  # Output: [3, 5, 8]

# Example Case 5
group1 = [1, 3, 7, 8]
group2 = [2, 5, 8, 10, 12]
shared_questions5 = find_shared_questions(group1, group2)
print(shared_questions5)  # Output: [8]

