'''
Pre Session 1 ==> Introductory lecture and discussion
Mentor and Facilitator ==> ANDY AFFUL

Pre Session 2
WEEK 2 PRE-SESSION ASSIGNMENT (16th July to 22nd July)
You are given a function that calculates the average score for a list of student scores. However, the
function has several issues and could benefit from code refactoring to improve readability and maintainability.
Your task is use your knowledge from the just ended Coding Without Borders programming class fix these issue.

Once you have completed the task, test the function with different inputs to ensure it produces the expected results.
Make sure to provide an explanation of the changes you made and how they address the bugs and code quality improvements.

This task will help you practice debugging, code refactoring, and improving code quality by addressing common issues
and applying best practices.
'''
def calc_average(scores):
    
    total_score = 0 #variable to keep track of total score
    number_of_scores = len(scores) #get total number os scores

    # check for an empty list
    if number_of_scores == 0:
        return 0
    
    #loop through the scores and get the sum total
    for score in scores:
        total_score += score
    
    #find the average score
    average = total_score / number_of_scores
    
    return round(average, 2) #return the average score rounded to 2 decimal places.


# CASE 1
score_list = [56, 75, 92, 88, 56]
print(calc_average(score_list))

# CASE 2
score_list2 = []
print(calc_average(score_list2))

# CASE 3
score_list3 = [56, 75.0, 92, 88.5]
print(calc_average(score_list3))

# CASE 4
score_list4 = [56, 75.0]
print(calc_average(score_list4))
#Output: 65.5

# CASE 5
score_list5 = [56, 75.0, 92, 88.5, 93, 77]
print(calc_average(score_list5))
#Output: 80.25