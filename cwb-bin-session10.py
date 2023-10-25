'''
SESSION 10 (11/09/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Merging Employee Lists

PROBLEM STATEMENT: Imagine you are working on an HR management system for a company that has recently acquired
another company. As part of the integration process, you need to merge the employee lists of both companies,
which are sorted by employee ID. Your task is to create a function that merges these two sorted employee lists
into a single sorted list.

Write a function:
def merge_employee_lists(company1_employees, company2_employees):
    # Your code here

INPUT: company1_employees and company2_employees are lists of employee IDs.
Both lists are sorted in ascending order.
Employee IDs are unique integers (1 <= ID <= 10^5).
The lengths of the lists can vary, but each list can have up to 10,000 employees.
Output:

OUTPUT: Return a single list containing all employee IDs from both companies, sorted in ascending order by
employee ID.

Example:
company1_employees = [101, 102, 105, 110]
company2_employees = [103, 104, 107, 108]
result = merge_employee_lists(company1_employees, company2_employees)
print(result)

Output:
[101, 102, 103, 104, 105, 107, 108, 110]
Notes:

The merged list should not contain duplicate employee IDs.
Your solution should not use any in-built sort function.
'''

