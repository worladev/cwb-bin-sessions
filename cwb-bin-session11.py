'''
SESSION 11 (13/09/2023)
Mentor and Facilitator ==> ANDY AFFUL

Title: "Election Results"

Problem Statement:

You have been given the results of a local election. Two lists are provided: one containing the names of the candidates, and the other containing
the number of votes each candidate received. Your task is to determine the winning candidate based on the highest number of votes. In the event
of a tie, return a list of the winning candidates' names.

Write a Python function find_winner(candidates, votes) that takes the following arguments:

candidates: A list of candidate identifiers (strings). The length of the list is between 1 and 1000.
votes: A list of integers representing the number of votes each candidate received. The length of this list matches the length of the candidates list.
The function should return a single winner (string) if there is no tie, or a list of winners (strings) in the event of a tie.

Example:

candidates = ["Candidate A", "Candidate B", "Candidate A", "Candidate C", "Candidate B", "Candidate A"]
votes = [3, 2, 3, 2, 8, 4]
winner = find_winner(candidates, votes)
print(winner)  # Output: ['Candidate A', 'Candidate B']
Explanation:

In this version of the problem, there is a tie between "Candidate A" and "Candidate B" since both received the highest number of votes (10 each).
Therefore, the function should return a list of the tied candidates' names.
'''