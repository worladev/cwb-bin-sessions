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
