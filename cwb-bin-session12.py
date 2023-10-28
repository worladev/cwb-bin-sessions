'''
SESSION 12 (18/09/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Count Strings Formed Using a Base String

PROBLEM STATEMENT: You are given a base string S and a list of strings L. Your task is to determine how many
strings from the list L can be formed using the characters of the base string S. A string can be formed if it
contains all the characters needed and doesn't have more characters than available in S.

Write a function count_strings_formed(S, L) to solve this problem.
Function Signature:
def count_strings_formed(S: str, L: List[str]) -> int:
    pass

INPUT:
S (1 <= len(S) <= 10^4): The base string containing lowercase letters.
L (1 <= len(L) <= 100): A list of strings, each containing lowercase letters.

OUTPUT: An integer representing the count of strings in list L that can be formed using the characters in string S.

Example 1:
S = "canopy"
L = ["copy", "nano", "can", "pan", "coy", "cane"]
count = count_strings_formed(S, L)
# Output: 4
# Explanation: All strings in L except "nano" and "cane" can be formed; "nano" requires 2 n's but's only 1 n,
# "cane" requires an 'e' but there's no 'e'

Example 2:
S = "programming"
L = ["program", "gram", "ping", "pong"]
count = count_strings_formed(S, L)
# Output: 4
# Explanation: All strings in L can be formed using the characters of "programming."

NOTE: needs refactoring.
counter = 0
for x in string k:
    if((x is both k and S) AND (count(x) in k <= count(x) in S)):
       counter += 1

string S = canopy
string k = "cane"
'''
from collections import Counter

def count_strings_formed(S, L):

    count = 0 # keep track of words that can be formed

    # check for empty string or list
    if S == "" or len(L) == 0:
        return count

    # count characters and their frequency in string
    s_word = Counter(S)
    indx = 0 #pointer variable

    #
    while indx < len(L):
        l_word = Counter(L[indx]) #get each word in list and count characters and their frequency
        if len(l_word - s_word) > 0: #if subtraction operation is greater than 0, ignore
            indx += 1 #increment pointer by 1
        else:
            count += 1
            indx += 1 #increment pointer by 1

    return count


# CASE 1:
S = "canopy"
L = ["copy", "nano", "can", "pan", "coy", "cane"]
count = count_strings_formed(S, L)
print(count)
# Output: 4

