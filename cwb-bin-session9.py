'''
SESSION 9 (06/09/2023)
Mentor and Facilitator ==> ANDY AFFUL

TASK 1
TITLE: "Analyzing Athlete's Training Progress"

PROBLEM STATEMENT: An athlete is preparing for a competition and records their training times over several days.
Your task is to write a Python program that finds and analyzes the improvement in their training times.

Write a function find_improvement(training_times) that takes the following argument:

INPUT: training_times: A list of integers representing the athlete's training times over consecutive days.
Each time value is less than  or greater than.
The function should find the longest sequence of consecutive days in which the athlete improved their training
times.
Improvement is defined as each training time being better than the previous day's time. Return the length of this
sequence as the result.

Example:
training_times = [3, 4, 6, 5, 5, 2, 4, 5, 6, 7, 6]
result = find_improvement(training_times)
print(result)  # Output: 4
Explanation:

In the provided training times, the athlete improved their times from day 6 to day 10:
Day 6: 2 (Improved)
Day 7: 4 (Improved)
Day 8: 5 (Improved)
Day 9: 6 (Improved)
Day 10: 7
The longest consecutive sequence of improvement is 4 days, from day 6 to day 10.
'''
