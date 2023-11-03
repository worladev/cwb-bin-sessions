'''
SESSION 16 (02/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Delivery Route Fuel Cost Calculation

PROBLEM STATEMENT: A delivery driver starts at a given starting point and needs to reach an ending point.
There are several intermediate points listed in a sequence.
The driver must visit these intermediate points in the given order. Your task is to calculate the total cost
of fuel used for the trip, considering the cost per kilometer.

Write a function
calculate_fuel_cost(start: Tuple[int, int], points: List[Tuple[int, int]], cost_per_km: float) -> float to solve this problem.

Function Signature:
def calculate_fuel_cost(start: Tuple[int, int], points: List[Tuple[int, int]], cost_per_km: float) -> float:
    pass

INPUT:
start: A tuple representing the starting point as (x, y) coordinates.
points: A list of tuples representing intermediate points. Each tuple is a (x, y) coordinate.
cost_per_km: A float representing the cost per kilometer of fuel.

OUTPUT: Returns a float representing the total cost of fuel used for the trip.

NOTE: Distance Calculation Formula:
The distance between two points (x1,y1) and (x2,y2) can be calculated using the Euclidean distance formula:

Example 1:

start = (0, 0)
points = [(1, 1), (2, 2), (3, 3), (4, 4)]
cost_per_km = 2.5  # $2.5 per kilometer

total_cost = calculate_fuel_cost(start, points, cost_per_km)
# Output: 14.14  # Assuming Euclidean distances between points
#Distance from (0, 0) to (1, 1): ≈1.41 (rounded to 2 decimal places)
#Distance from (1, 1) to (2, 2): ≈1.41 (rounded to 2 decimal places)
#Distance from (2, 2) to (3, 3): ≈1.41 (rounded to 2 decimal places)
#Distance from (3, 3) to (4, 4): ≈1.41 (rounded to 2 decimal places)
#Total distance traveled: 1.41 + 1.41 + 1.41 + 1.41 = 5.64 (rounded to 2 decimal places)
1.41+1.41+1.41+1.41=5.64 (rounded to 2 decimal places)

Therefore, the total cost is
5.64 * 2.5 =  14.10 (rounded to 2 decimal places).

Example 2:
start = (2, 4)
points = [(2,0),(-1,2),(-3,3},(2,7),(4,-4)]
cost_per_km = 3.3  # $3.3 per kilometer
total_cost = calculate_fuel_cost(start, points, cost_per_km)
#total_cost = $90.5
'''
from math import sqrt

def calculate_fuel_cost(start, points, cost_per_km):

    total_distance = 0 #variable to hold total distance covered
    total_cost = 0.0

    #check for empty start and subsequent points
    if len(start) == 0 or len(points) == 0 or cost_per_km == 0:
      return total_cost

    st = start #the start cordinates
    i = 0 #keep track of cordinates in points

    while i < len(points):
        x_val = (points[i][0] - st[0])**2
        y_val = (points[i][1] - st[1])**2
        distance = round(sqrt(x_val + y_val), 2) #compute distance between the two points
        total_distance += distance #compute total distance

        st = points[i] #set starting point to the last points in previous distance
        i += 1 #increment tracker by 1

    #calculate total cost and round to 2 decimal places
    total_cost = round((total_distance * cost_per_km), 2)

    #return the total cost
    return total_cost


# CASE 1
start = (0, 0)
points = [(1, 1), (2, 2), (3, 3), (4, 4)]
cost_per_km = 2.5  # $2.5 per kilometer
total_cost = calculate_fuel_cost(start, points, cost_per_km)
print(total_cost)
# Output: 14.14
