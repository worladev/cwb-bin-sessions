'''
SESSION 20 (16/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Roman Converter

PROBLEM STATEMENT: Create a class RomanConverter with a method roman_to_int(roman: str) -> int that takes a Roman numeral as input and returns
the corresponding integer. The input Roman numeral will be guaranteed to be a valid Roman numeral representation.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example:
roman_converter = RomanConverter()
print(roman_converter.roman_to_int("III"))  # Output: 3
print(roman_converter.roman_to_int("IX"))   # Output: 9
print(roman_converter.roman_to_int("LVIII"))# Output: 58
print(roman_converter.roman_to_int("MCMXCIV"))# Output: 1994

Constraints:
The input Roman numeral string s is guaranteed to be a valid Roman numeral where 1 <= s.length <= 15.
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.
'''

from enum import IntEnum

# Enum class to hold all seven unique roman values
class RomanNumerals(IntEnum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

# RomanConverter class
class RomanConverter:
    def __init__(self):
        self.enum_val = RomanNumerals

    def roman_to_int(self, roman):
        length_of_numeral = len(roman) #length of the user input roman numerals
        index = 0 #tracker variable
        int_value = 0 #variable to hold integer value of roman numeral

        while index < length_of_numeral:
            #using connectives to compare and compute values of current and previous index
            if index > 0 and self.enum_val[roman[index]] > self.enum_val[roman[index-1]]:
                value = self.enum_val[roman[index]] - self.enum_val[roman[index-1]]
                int_value += (value - self.enum_val[roman[index-1]])
            else:
                int_value += self.enum_val[roman[index]]

            index += 1 #increment index value by 1

        return int_value


#creating instance of the RomanConverter class
roman_converter = RomanConverter()

#Example Cases
print(roman_converter.roman_to_int("III"))  # Output: 3

