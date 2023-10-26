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
def find_winner(candidates, votes):

  #return none if parameter is empty
  if len(candidates) == 0 or len(votes) == 0:
    return None

  #variables
  total_votes = dict() #hold candidates and the total votes accrued
  highest_vote = list() #hold candidate(s) with the highest votes
  pointer = 0 #pointer variable to candidate list

  #loop to get candidate and their total votes
  for candidate in candidates:
    total_votes[candidate] = total_votes.get(candidate, 0) + votes[pointer]
    pointer += 1

  #list comprehension to get the candidate(s) with the highest votes
  highest_vote = [key for key, value in total_votes.items() if value == max(total_votes.values())]

  return highest_vote #return the candidate(s) with the highest votes


# CASE 1
candidates = ["Candidate A", "Candidate B", "Candidate A", "Candidate C", "Candidate B", "Candidate A"]
votes = [3, 2, 3, 2, 8, 4]
winner = find_winner(candidates, votes)
print(winner)  # Output: ['Candidate A', 'Candidate B']

# CASE 2
candidates2 = ["Candidate A", "Candidate B", "Candidate A", "Candidate C", "Candidate B", "Candidate A"]
votes2 = [4, 1, 5, 6, 7, 3]
winner2 = find_winner(candidates2, votes2)
print(winner2)  # Output: ['Candidate A']

# CASE 3
candidates3 = ["Candidate A", "Candidate B", "Candidate A", "Candidate C", "Candidate B"]
votes3 = []
winner3 = find_winner(candidates3, votes3)
print(winner3)  # Output: None
