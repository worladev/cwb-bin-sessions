'''
IN SESSION 22 CODING CHALLENGE (25/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Maximum number of candies you can eat.

PROBLEM STATEMENT: You are given totalCandies initial candies. The candy store has a promotion: you can exchange
wrapperExchange empty candy wrappers for one additional candy. You eat the candies and exchange the wrappers
until you can no longer make an exchange. Write a function maxCandies(totalCandies, wrapperExchange) to calculate
the maximum number of candies you can eat.

INPUT:
totalCandies: An integer representing the initial number of candies you have (1 <= totalCandies <= 10^5).
wrapperExchange: An integer representing the number of empty wrappers required to get one additional candy (2 <= wrapperExchange <= 100).

OUTPUT:
Return an integer representing the maximum number of candies you can eat.

Function Signature:
def maxCandies(totalCandies: int, wrapperExchange: int) -> int:

Example 1:
totalCandies = 25
wrapperExchange = 4
print(maxCandies(totalCandies, wrapperExchange))  # Output: 31

Explanation:
You start with 25 candies.
Exchange 24 wrappers for 6 additional candies (total candies now: 25 initial + 6 exchanged = 31).
You now have 6 wrappers remaining.
Exchange 6 wrappers for 1 additional candy (total candies now: 31 initial + 1 exchanged = 32).
You now have 1 wrapper remaining, which is not enough to exchange for more candies.

Example 2:
totalCandies = 15
wrapperExchange = 3
print(maxCandies(totalCandies, wrapperExchange))  # Output: 21

Explanation:
You start with 15 candies.
Exchange all 15 candies for 5 additional candies (total candies now: 15 initial + 5 exchanged = 20).
You now have 5 wrappers remaining.
Exchange 3 wrappers for 1 additional candy (total candies now: 20 initial + 1 exchanged = 21).
You now have 2 wrappers remaining, which are not enough to exchange for more candies.

Example 3:
totalCandies = 50
wrapperExchange = 7
print(maxCandies(totalCandies, wrapperExchange))  # Output: 58

Explanation:
You start with 50 candies.
Exchange 49 candies for 7 additional candies (total candies now: 50 initial + 7 exchanged = 57).
You now have 7 wrappers remaining.
Exchange all 7 wrappers for 1 additional candy (total candies now: 50 initial + 7 exchanged + 1 exchanged = 58).
'''
def maxCandies(totalCandies, wrapperExchange):
    candiesleft = totalCandies # variable to hold total candies left
    maxCandies = totalCandies # variable to hold maximum candies that can be eaten.

    # loop to compute maximum candies that can be eaten
    while candiesleft >= wrapperExchange:
        extraCandy = totalCandies // wrapperExchange
        maxCandies += extraCandy
        candiesleft = extraCandy
        totalCandies = candiesleft # total candies is set to candies left

    return maxCandies #return maximum candies that can be eaten



# Example 1:
totalCandies = 25
wrapperExchange = 4
print(maxCandies(totalCandies, wrapperExchange))  # Output: 32

# Example 2:
totalCandies = 15
wrapperExchange = 3
print(maxCandies(totalCandies, wrapperExchange))  # Output: 21

# Example 3:
totalCandies = 50
wrapperExchange = 7
print(maxCandies(totalCandies, wrapperExchange))  # Output: 58

