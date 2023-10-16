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
#use inbuilt functions to simplify code

from math import sqrt
from collections import Counter

def curved_grading(scores):

   #variable declaration
   score_count = dict()
   unique_scores = set()
   modes = list()
   modal_score = 0

   #check for empty score list
   if len(scores) == 0:
       return None

   #iterate through the scores and add each of them to score_count variable as
   # key and the number of times it appears as the value
   score_count = Counter(scores)

   for score in scores:
        if score in score_count:
            score_count[score] += 1
        else:
            score_count[score] = 1

   #get unique scores and save them in a new list variable
   for key, value in score_count.items():
       if value == 1:
           unique_scores.add(key)
       elif value == max(score_count.values()):
           modes.append(key)
           modal_score = max(modes)

   #get the total number of valid scores (i.e unique scores and the modal score)
   number_of_scores = len(unique_scores) + 1

   #get the total of all the scores
   total = sum(unique_scores) + modal_score

   #calculate average score
   average = total/number_of_scores

   #calculate curved grade
   curved_grade = round(sqrt(average), 2)

   return curved_grade

