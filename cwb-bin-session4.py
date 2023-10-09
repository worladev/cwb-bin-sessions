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
def plan_meals(breakfast_prices, supper_prices, daily_budget):
    
    # a list variable possible_meals to hold all valid daily meals within budget.
    possible_meals = list()

    # a tuple variable to hold one valid meal within budget.
    meal = tuple()

    # a condition to return an empty list if any input item has no element in it.
    if len(breakfast_prices) == 0 or len(supper_prices) == 0 or daily_budget == 0:
        return possible_meals

    # a nested loop that get each breakfast price and supper price.
    # add them, if the sum falls within the daily budget add it to the
    # possible_meal list as a tupple object.
    for i in breakfast_prices:
        for j in supper_prices:
            if i == 0 or j == 0 or daily_budget == 0:
                continue
            elif i + j <= daily_budget:
                meal = (i, j)
                possible_meals.append(meal)

    return possible_meals


# Example Case 1
breakfast_prices = [5, 7, 3, 10]
supper_prices = [8, 5, 9, 7]
daily_budget = 14
possible_meal = plan_meals(breakfast_prices, supper_prices, daily_budget)
print(possible_meal)

# Example Case 2 - one empty argument
breakfast_prices2 = [5, 7, 3, 10]
supper_prices2 = []
daily_budget2 = 14
possible_meal2 = plan_meals(breakfast_prices2, supper_prices2, daily_budget2)
print(possible_meal2)

# Example Case 3 - floating point values for some prices
breakfast_prices3 = [5, 7.59, 3, 10.99]
supper_prices3 = [8.58, 5, 9.99, 7.5]
daily_budget3 = 14
possible_meal3 = plan_meals(breakfast_prices3, supper_prices3, daily_budget3)
print(possible_meal3)

# Example Case 4 - invalid prices
breakfast_prices4 = [5, 0, 0, 0]
supper_prices4 = [8, 5, 9, 7]
daily_budget4 = 14
possible_meal4 = plan_meals(breakfast_prices4, supper_prices4, daily_budget4)
print(possible_meal4)

# Example Case 5 - no budget
breakfast_prices5 = [5, 7, 3, 10]
supper_prices5 = [8, 5, 9, 7]
daily_budget5 = 0
possible_meal5 = plan_meals(breakfast_prices5, supper_prices5, daily_budget5)
print(possible_meal5)

