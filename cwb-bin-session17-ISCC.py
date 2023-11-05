'''
IN SESSION 17 CODING CHALLENGE (04/10/2023)
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
def excel_column_to_number(column_title):

    number = 0 #variable to hold column title number value

    i = 0 #index tracker

    #loop to get each alphabet in column title
    while i < len(column_title):
        number *= 26 #default base 26

        #subtract the ascii value of letter "A" from the value of letter at index i
          # add 1 and add it to value of number variable.
        number += ord(column_title[i]) - ord('A') + 1
        i += 1 #increment tracker by 1

    return number


# Example Cases:
print(excel_column_to_number('A'))  # Output: 1
print(excel_column_to_number('AC'))  # Output: 30
print(excel_column_to_number('ZZ'))  # Output: 702
print(excel_column_to_number('C'))  # Output: 3
print(excel_column_to_number('AA'))  # Output: 27
print(excel_column_to_number('AB'))  # Output: 28
print(excel_column_to_number('Z'))  # Output: 26

