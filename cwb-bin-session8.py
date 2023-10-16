'''
SESSION 8 (30/08/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: "Curved Grading System"

PROBLEM STATEMENT: An instructor needs to grade a math test using a curved grading system. In this system,
the instructor calculates the average of the unique scores and the modal score obtained by the students and
then takes the square root of that average to assign the final grades.
Your task is to write a Python program to implement this grading system.

INSTRUCTION: Implement a Python function curved_grading(scores) that takes the following argument:

scores: A list of integers representing the scores obtained by students in a math test. Each score is
between 0 and 100.
The function should calculate the average of the unique scores and then take the square root of that
average. Round the result to two decimal places and return it as the final grade.

Example Case:
scores = [90 90 90 80 75 65 65]
final_grade = curved_grading(scores)
print(final_grade)  # Output: 9.04

Explanation:
Modal score: 90
Unique scores in the list: [80, 75]
Average of unique scores with modal score(90): 90 + (80 + 75) / 3 = 81.6667
Square root of the average: √81.6666666667 ≈ 9.04
'''
