'''
IN SESSION 15 CODING CHALLENGE (29/09/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: "Pangram Checker"

PROBLEM STATEMENT: A pangram is a sentence that contains every letter of the alphabet at least once. Your task
is to write a Python function is_pangram(sentence) that checks if a given sentence is a pangram or not.

OUTPUT: The function should return True if the sentence is a pangram and False otherwise.

Example:
sentence1 = "The quick brown fox jumps over the lazy dog"
result1 = is_pangram(sentence1)
print(result1)
# Output: True

sentence2 = "Hello, World!"
result2 = is_pangram(sentence2)
print(result2)
# Output: False
'''
def is_pangram(sentence):
  # Create a list to track the presence of each letter (a to z).
  arr = [0] * 26

  for char in sentence:
    char = char.lower()
    if 'a' <= char and char <= 'z':
      # Calculate the index in the list for the character.
      index = ord(char) - ord('a')

      # Mark the presence of the character by setting its value to 1.
      arr[index] = 1

  # Check if all letters (values) in the list are 1, indicating a pangram.
  return all(arr)


# Example Case 1:
sentence1 = "The quick brown fox jumps over the lazy dog"
result1 = is_pangram(sentence1)
print(result1)
# Output: True

# Example Case 2:
sentence2 = "Hello, World!"
result2 = is_pangram(sentence2)
print(result2)
# Output: False

# Example Case 3:
sentence3 = "abcdefghijklmnopqrsuvwxyz"
result3 = is_pangram(sentence3)
print(result3)
# Output: False
