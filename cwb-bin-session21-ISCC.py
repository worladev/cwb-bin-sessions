'''
IN SESSION 21 CODING CHALLENGE (23/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Peak Oxygen Level in a Training Session

PROBLEM STATEMENT: Alice is an athlete training to increase her blood oxygen level during a workout session.
She records her blood oxygen levels at different time intervals and organizes them into an array oxygen_levels
where oxygen_levels[i] represents her blood oxygen level at time i. The training session follows the pattern

Initially, Alice's blood oxygen level is low and gradually increases. At a certain point, her oxygen level
reaches a peak. After the peak, it starts decreasing. Alice wants to find out the time when she reached her
peak oxygen level.

Write a function find_peak_time(oxygen_levels: List[int]) -> int to help her determine the index corresponding to her peak oxygen level.

INPUT:
oxygen_levels: A list of integers [oxygen_levels[0], oxygen_levels[1], ..., oxygen_levels[n-1]] where 1 ≤ n ≤ 10^6 and
80 ≤ oxygen_levels[i] ≤ 100. The values represent Alice's blood oxygen levels during the training session.

OUTPUT:
Return an integer representing the time index when Alice reached her peak oxygen level.

Example:
oxygen_levels = [85, 88, 92, 95, 97, 96, 94, 91, 89, 86, 84]
find_peak_time(oxygen_levels)

Output: 4
Explanation:
In the given example, Alice's peak oxygen level is 97 which occurs at index 4 in the oxygen_levels array.

3 Approaches
-------------
- Use the in built max() method to find the max element
- Use normal linear search where we inspect from the 2nd to last but 1 element
   85, 88, 92, 95, 97, 96, 94, 91, 89, 86, 84
   = currentNumber, previousNumber, nextNumber
   peakNumber =>  previous < currentNumber > nextNumber
- Use binary search
    mid = low + (high-low)/2
    peak = list[mid - 1] < list[mid] > list[mid + 1]
     
    if(list[mid+1] < list[mid]):
        upper = mid - 1
    else:
        lower = mid + 1
'''
# SOLUTION 1 -using in-built max function
def find_peak_time(oxygen_levels):
    
    # return none if oxygen levels list is empty
    if len(oxygen_levels) == 0:
        return None
    
    # return the index of the maximum oxygen level
    peak = oxygen_levels.index(max(oxygen_levels))
    return peak


# Example Case:
oxygen_levels = [85, 88, 92, 95, 97, 96, 94, 91, 89, 86, 84]
print(find_peak_time(oxygen_levels)) # Output: 4


# SOLUTION 2 -using linear search
def find_peak_time2(oxygen_levels):
    # using negative infinity as initial maximum value
    max_value = float('-inf')
    
    for val in range(len(oxygen_levels)):
        if oxygen_levels[val] > max_value:
            max_value = oxygen_levels[val]
            max_indx = oxygen_levels.index(max_value)
    return max_indx


