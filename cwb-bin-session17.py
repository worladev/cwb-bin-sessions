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
# SOLUTION 1

def count_faulty_servers(classifications):

    segregate = dict() #dictionary to hold performance of each server
    count_faulty_servers = 0 #tracker to keep count of faulty servers

    #loop to assign performance value to each server
    for item in range(1, len(classifications), 2):
        if classifications[item] not in segregate:
            segregate[classifications[item]] = [classifications[item-1]]
        else:
            segregate[classifications[item]] += [classifications[item-1]]

    #loop to check for faulty servers
    for value in segregate.values():
        if "H" in value and "M" in value and "L" in value:
            count_faulty_servers += 1 #increment faulty server value by 1

    return count_faulty_servers #return number of faulty servers


# Example 1:
rings = "L1H1H2M4L4L1L1M3H1H1M1H1"
result = count_faulty_servers(rings)
print(result)
# Output: 1

# Example 2:
rings2 = "M2M4L0M1L0L0L4L1L0M3L0M2L3H4L0M3H4H4"
result2 = count_faulty_servers(rings2)
print(result2)
# Output: 1

# Example 3:
rings3 = "L0L3M1M1H2L1L1L3M1H0L4L3H0L3L3H3H3L1"
result3 = count_faulty_servers(rings3)
print(result3)
# Output: 0

# Example 4:
rings4 = "L0M1H2L0M4H1M4L2H3H2M0H4L0H4H2M1M1H0M2L4"
result4 = count_faulty_servers(rings4)
print(result4)
# Output: 3



############# SOLUTION 2 #################
# Code by Andy
def count_faulty_servers(testResults):
    count = 0
    HIGH, MEDIUM, LOW = 0, 1, 2
    mask = 0b111
    length = len(testResults)
    masks = [0] * (length // 2)

    for i in range(0, length - 1, 2):
        color = testResults[i]
        server = int(testResults[i + 1])

        if color == 'H':
            masks[server] |= (1 << HIGH)
        elif color == 'M':
            masks[server] |= (1 << MEDIUM)
        elif color == 'L':
            masks[server] |= (1 << LOW)

    for maskVal in masks:
      #an exclusive or between maskVal and mask
        if maskVal ^ mask == 0:
            count += 1

    return count


# Same test cases for solution 1 plus 2 new.
# Example 1:
rings = "L1H1H2M4L4L1L1M3H1H1M1H1"
result = count_faulty_servers(rings)
print(result)
# Output: 1

# Example 2:
rings2 = "M2M4L0M1L0L0L4L1L0M3L0M2L3H4L0M3H4H4"
result2 = count_faulty_servers(rings2)
print(result2)
# Output: 1