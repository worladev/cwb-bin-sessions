'''
SESSION 17 (04/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Faulty Servers Detection

PROBLEM STATEMENT: You are analyzing the performance of n servers in a company, each labeled from 1 to n.
The performance of each server is classified as HIGH ('H'), MEDIUM ('M'), or LOW ('L'). The analysis results in a
string output of length 2n, where every two characters represent a classification-server pair.

- The first character of each pair represents the server's classification ('H', 'M', or 'L').
- The second character of each pair represents the server from which the classification originated ('1' to 'n').

A server is considered faulty if, for a given test run, it returned all three classifications: HIGH, MEDIUM,
and LOW. You need to identify and count the number of faulty servers.

Implement a function count_faulty_servers(classifications: str, n: int) -> int:

Function Signature:
def count_faulty_servers(classifications: str, n: int) -> int:
    pass

INPUT:
classifications: A string of length 2n containing classifications of servers in the format 'H1M2L3',
where 'H1' indicates HIGH classification from server 1, 'M2' indicates MEDIUM classification from server 2,
and so on. (1 <= n <= 100)
n: An integer representing the number of servers (1 <= n <= 100)

OUTPUT: Returns an integer representing the number of faulty servers.

Note:
You need to identify servers that have returned all three classifications: HIGH, MEDIUM, and LOW, and count them as faulty.
The input string will always be of valid format and length kn, where k is an integer and n the number of servers.
'''
