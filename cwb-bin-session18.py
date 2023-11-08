'''
SESSION 18 (09/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

PROBLEM STATEMENT: You are tasked with implementing a mini-Sudoku verification algorithm. Mini-Sudoku is played
on a 3x3 grid, where each row and column contain unique integers from 1 to 3.

Write a Python class MiniSudoku with the following functionalities:

- Initialization: The class should initialize with a 3x3 grid (a list of lists) where each element is initially
set to 0. This grid will represent the Sudoku puzzle.
- Method set_value(row, col, value): This method should set the value at the given row and column (both 0-indexed)
to the provided integer value (from 1 to 3).
- Method is_valid() -> bool: This method should return True if the partially filled grid is a valid mini-Sudoku
configuration and False otherwise.

# Example1 Usage:
sudoku = MiniSudoku()
sudoku.set_value(3, 2, 1)
sudoku.set_value(2, 1, 3)
sudoku.set_value(1, 3, 2)

print("Is the Sudoku valid?", sudoku.is_valid())  # Output: True

# Example2 Usage:
sudoku = MiniSudoku()
sudoku.set_value(1, 3, 2)
sudoku.set_value(2, 1, 3)
sudoku.set_value(3, 2, 1)

print("Is the Sudoku valid?", sudoku.is_valid())  # Output: True

# Example2 Usage:
sudoku = MiniSudoku()
sudoku.set_value(3, 1, 2)
sudoku.set_value(2, 1, 3)
sudoku.set_value(1, 2, 3)

print("Is the Sudoku valid?", sudoku.is_valid())  # Output: False
'''
class MiniSudoku:
    # an init method to initialize a 3x3 grid of nested list and
      # and set initial element value to 0
    def __init__(self, n):
        self.grid = [[0]*n]*n
        self.maxRow = n
        self.maxColumn = n

    # a set_value method to set values at a given row and column in the 3x3 grid
    def set_value(self, row, col, value):
        if row <= self.maxRow and col <= self.maxColumn:
            self.grid[row-1][col-1] = value


    def is_valid(self):
        n = len(self.grid)
        row_check = [False] * n
        col_check = [False] * n

        # Check each row and column
        for i in range(n):
            row_check = [False] * n
            col_check = [False] * n

            for j in range(n):

                # Check rows
                row_value = self.grid[i][j]

                #if the value is outside 1-n or we've seen it before, return false
                if row_value < 1 or row_value > n or row_check[row_value - 1]:
                    return False

                #mark the value as seen
                row_check[row_value - 1] = True

                # Check columns
                col_value = self.grid[j][i]

                if col_value < 1 or col_value > n or col_check[col_value - 1]:
                    return False

            col_check[col_value - 1] = True

        return True
    

# Example1 Usage:
sudoku1 = MiniSudoku(3)
sudoku1.set_value(3, 2, 1)
sudoku1.set_value(2, 1, 3)
sudoku1.set_value(1, 3, 2)
print("Is the Sudoku valid?", sudoku1.is_valid())  # Output: True

# Example2 Usage:
sudoku2 = MiniSudoku(3)
sudoku2.set_value(1, 3, 2)
sudoku2.set_value(2, 1, 3)
sudoku2.set_value(3, 2, 1)
print("Is the Sudoku valid?", sudoku2.is_valid())  # Output: True

# Example3 Usage:
sudoku3 = MiniSudoku(3)
sudoku3.set_value(3, 1, 2)
sudoku3.set_value(2, 1, 3)
sudoku3.set_value(1, 2, 3)
print("Is the Sudoku valid?", sudoku3.is_valid())  # Output: False

# Example4 Usage:
sudoku4 = MiniSudoku(3)
sudoku4.set_value(1, 1, 2)
sudoku4.set_value(2, 2, 2)
sudoku4.set_value(3, 3, 3)
print("Is the Sudoku valid?", sudoku4.is_valid())  # Output: False

# Example5 Usage:
sudoku5 = MiniSudoku(3)
sudoku5.set_value(1, 1, 1)
sudoku5.set_value(2, 2, 2)
sudoku5.set_value(3, 3, 3)
print("Is the Sudoku valid?", sudoku5.is_valid())  # Output: True
