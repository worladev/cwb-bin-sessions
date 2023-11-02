'''
SESSION 15 (29/09/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Grouping Anagrams for Crossword Puzzles

PROBLEM STATEMENT: In the world of Crossword Puzzles, it's essential to find words that fit within a given set
of blanks. To aid crossword enthusiasts, your task is to write a program that can efficiently group anagrams from
a list of words. Anagrams are words or phrases formed by rearranging the letters of another word or phrase,
using all the original letters exactly once.

For example, the words "listen," "enlist," and "tinsel" are all anagrams of each other because they share the same
set of letters, just rearranged differently. Write a Python function group_anagrams(word_list) that takes a list
of words as input and returns a list of groups, where each group consists of words that are anagrams of each other.

Function Signature:
def group_anagrams(word_list: List[str]) -> List[List[str]]:

INPUT: word_list (1 <= len(word_list) <= 1000): A list of words containing only lowercase alphabetical characters.
The length of each word will not exceed 100 characters.

OUTPUT: A list of lists, where each inner list represents a group of anagrams. The order of groups and the order
of words within each group does not matter.

Example:
word_list = ["listen", "enlist", "silent", "hello", "world"]
result = group_anagrams(word_list)

Output:
[
    ["listen", "enlist", "silent"],
    ["hello"],
    ["world"]
]
'''
