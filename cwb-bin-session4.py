'''
SESSION 4 (16/08/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Meal Planning on a Budget

PROBLEM STATEMENT: You are a university student trying to plan your meals for the week while staying within
a tight budget. You have a fixed budget for each day, and you want to figure out the best combination of
breakfas, and supper that you can afford while skipping lunch. Your task is to write a Python program that
takes three lists of meal prices and a daily budget and returns a list of possible daily meal plans you can afford.

INSTRUCTIONS: Implement a Python function plan_meals(breakfast_prices, supper_prices, daily_budget) that takes
the following arguments:

INPUT:
breakfast_prices: A list of prices for various breakfast meals.
supper_prices: A list of prices for various supper meals.
daily_budget: An integer representing your daily budget.

breakfast_prices = [5, 7, 3, 10]
supper_prices = [8, 5, 9, 7]
daily_budget = 14

possible_meals = plan_meals(breakfast_prices, supper_prices, daily_budget)
print(possible_meals)

#OUTPUT:
[5, 8]
[5, 5]
[5, 9]
[5, 7]
[7, 5]
[7, 7]
[3, 8]
[3, 5]
[3, 9]
[3, 7]

Hint: Consider using tuples to represent daily meal plans, where each tuple contains a breakfast and
supper combination. You can then store these tuples in a list to keep track of all the possible meal
plans within your budget.
'''