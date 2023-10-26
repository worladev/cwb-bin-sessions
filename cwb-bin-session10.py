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
def merge_employee_lists(listA, listB):

    # return the other list if a list is empty
    if len(listA) < 1:
        return listB
    if len(listB) < 1:
        return listA

    mergedList = list() # list variable to hold merged ID's
    
    pointerA, pointerB = 0, 0 # pointer variables to listA and listB

    while pointerA < len(listA) and pointerB < len(listB):
        fromA = listA[pointerA]
        fromB = listB[pointerB]
        
        if fromA < fromB: # check if first list ID is less than second list ID
            mergedList.append(fromA) # if true, append first list ID
            pointerA += 1  # increment list A pointer by 1
        elif fromA > fromB: # check if the two lists ID are the same
            mergedList.append(fromB)
            pointerB += 1 # increment list B pointer by 1
        else:
            mergedList.append(fromB)
            pointerA += 1 # increment list A pointer by 1
            pointerB += 1 # increment list B pointer by 1

    # add the rest of the items in the longer list to the merged list
    if pointerA < len(listA):
        mergedList.extend(listA[pointerA:])
    if pointerB < len(listB):
        mergedList.extend(listB[pointerB:])

    return mergedList

# CASE 1
company1_employees = [101, 102, 105, 110]
company2_employees = [103, 104, 107, 108]
result = merge_employee_lists(company1_employees, company2_employees)
print(result)
#Output: [101, 102, 103, 104, 105, 107, 108, 110]

# CASE 2
company1_employees2 = [101, 102, 103, 105, 110]
company2_employees2 = [103, 104, 107, 108]
result2 = merge_employee_lists(company1_employees2, company2_employees2)
print(result2)
#Output: [101, 102, 103, 104, 105, 107, 108, 110]

# CASE 3
company1_employees3 = []
company2_employees3 = []
result3 = merge_employee_lists(company1_employees3, company2_employees3)
print(result3)
#Output: []

# CASE 4
company1_employees4 = [101, 102, 105, 110]
company2_employees4 = []
result4 = merge_employee_lists(company1_employees4, company2_employees4)
print(result4)
# Output: [101, 102, 105, 110]

# CASE 5
company1_employees5 = [101, 102, 105, 110]
company2_employees5 = [101, 104, 107, 108]
result5 = merge_employee_lists(company1_employees5, company2_employees5)
print(result5)
#Output: [101, 102, 104, 105, 107, 108, 110]