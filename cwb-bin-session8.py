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

   #get the count of each score as a key value pair
   score_count = Counter(scores)

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



# Example- case 1 mode:90
scores = [90, 90, 90, 80, 75, 65, 65]
final_grade = curved_grading(scores)
print(final_grade) #Output: 9.04

# Example- case 2 mode:0
scores2 = []
final_grade2 = curved_grading(scores2)
print(final_grade2) #Output: None

# Example- case 3 mode:95
scores3 = [90, 90, 90, 80, 75, 65, 65, 95, 95, 95]
final_grade3 = curved_grading(scores3)
print(final_grade3) #Output: 9.13

# Example- case 4 mode:80
scores4 = [90, 80, 80, 75, 65, 95]
final_grade4 = curved_grading(scores4)
print(final_grade4) #Output: 9.0

# Example- case 5 mode:65
scores5 = [90, 80, 75, 65, 65, 65, 95]
final_grade5 = curved_grading(scores5)
print(final_grade5)  # Output: 9.0

# Example- case 6 mode:50
scores6 = [90, 80, 75, 65, 50, 50]
final_grade6 = curved_grading(scores6)
print(final_grade6)  # Output: 8.49

# Example- case 7 mode:80
scores7 = [90, 80, 80, 75, 65, 50, 50]
final_grade7 = curved_grading(scores7)
print(final_grade7)  # Output: 8.8