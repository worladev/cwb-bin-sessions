'''
SESSION 13 (20/09/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Temperature Data Transformation

PROBLEM STATEMENT: You are working on a weather monitoring application that collects temperature data from various weather stations. The temperature
data is recorded as a square matrix, where each row represents a weather station, and each column represents a time interval. Your
task is to process this temperature data to make it more useful for analysis.

Write a function transform_temperature_data(matrix) that takes a square temperature matrix as input and returns a transposed matrix
where each row represents a time interval, and each column represents a weather station.

Function Signature:
def transform_temperature_data(matrix: List[List[float]]) -> List[List[float]]:
    pass

INPUT:
matrix (List[List[float]]): A square temperature matrix represented as a 2D list of lists. The matrix has dimensions n x n, where n
represents the number of weather stations (rows) and time intervals (columns). Each element of the matrix represents the temperature
recorded at a specific station and time interval. The temperature values are floating-point numbers.

OUTPUT:
Returns a new matrix where each row represents a time interval, and each column represents a weather station. The matrix is a transpose
of the input matrix.

Example:
temperature_data = [
    [72.5, 73.0, 72.8],
    [71.2, 71.8, 71.0],
    [70.5, 70.2, 70.9]
]

transformed_data = transform_temperature_data(temperature_data)
# Output:
# [
#   [72.5, 71.2, 70.5],
#   [73.0, 71.8, 70.2],
#   [72.8, 71.0, 70.9]
# ]
'''
def transform_temperature_data(matrix):
    
    if matrix is None: # return none if matrix value is none
        return None
    
    transformed_matrix = list() # list variable for transformed matrix
    
    # loop to perform transformation
    for row in range(len(matrix)):
        new_row = list()
        for col in range(len(matrix[row])):
            new_row.append(matrix[col][row])
        transformed_matrix.append(new_row)
    
    return transformed_matrix # return transformed matrix


# CASE 1:
temperature_data = [
  [72.5, 73.0, 72.8],
  [71.2, 71.8, 71.0],
  [70.5, 70.2, 70.9]
]
transformed_data = transform_temperature_data(temperature_data)
# print(transformed_data)
for row in transformed_data:
  print(row)
# Output:
#  [
  #  [72.5, 71.2, 70.5],
  #  [73.0, 71.8, 70.2],
  #  [72.8, 71.0, 70.9]
#  ]
