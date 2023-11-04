'''
SESSION 17 (04/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Excel Column Title to Number Conversion

PROBLEM STATEMENT: In various data processing scenarios, there's a need to convert Excel column titles to corresponding
numbers for effective analysis. In Excel, column titles are represented by uppercase English letters
('A' to 'Z', 'AA' to 'ZZ', and so on). Write a function excel_column_to_number(column_title: str) -> int to convert
an Excel column title to the corresponding number.

Function Signature:
def excel_column_to_number(column_title: str) -> int:

INPUT:
column_title: A string containing uppercase English letters, where 1 \leq \text{len(column_title)} \leq 7.

OUTPUT:
Returns an integer representing the corresponding column number.

Example:
print(excel_column_to_number('A'))  # Output: 1
print(excel_column_to_number('AC'))  # Output: 30
print(excel_column_to_number('ZZ'))  # Output: 702
'''