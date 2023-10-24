'''
SESSION 9 (06/09/2023)
Mentor and Facilitator ==> ANDY AFFUL

TASK 1
TITLE: "Analyzing Athlete's Training Progress"

PROBLEM STATEMENT: An athlete is preparing for a competition and records their training times over several days.
Your task is to write a Python program that finds and analyzes the improvement in their training times.

Write a function find_improvement(training_times) that takes the following argument:

INPUT: training_times: A list of integers representing the athlete's training times over consecutive days.
Each time value is less than  or greater than.
The function should find the longest sequence of consecutive days in which the athlete improved their training
times.
Improvement is defined as each training time being better than the previous day's time. Return the length of this
sequence as the result.

Example:
training_times = [3, 4, 6, 5, 5, 2, 4, 5, 6, 7, 6]
result = find_improvement(training_times)
print(result)  # Output: 4
Explanation:

In the provided training times, the athlete improved their times from day 6 to day 10:
Day 6: 2 (Improved)
Day 7: 4 (Improved)
Day 8: 5 (Improved)
Day 9: 6 (Improved)
Day 10: 7
The longest consecutive sequence of improvement is 4 days, from day 6 to day 10.
'''
def find_improvement(training_times):
  
  # check if there is only one or no training times available
  if len(training_times) <= 1:
    return None

  #single line multi-variable declaration
  maximum_length = length_of_sequence = 0

  for indx in range(len(training_times)):
    if training_times[indx] > training_times[indx - 1]:
      length_of_sequence += 1
    else:
      length_of_sequence = 0

    #getting the longest sequence of improvement in training times
    maximum_length = max(length_of_sequence, maximum_length)

  return maximum_length


#CASE 1:
training_times = [3, 4, 6, 5, 5, 2, 4, 5, 6, 7, 6]
result = find_improvement(training_times)
print(result)  # Output: 4

#CASE 2:
training_times2 = [4, 4, 5, 4, 5, 4, 4, 5, 3, 5, 6]
result2 = find_improvement(training_times2)
print(result2)  # Output: 2

#CASE 3:
training_times3 = []
result3 = find_improvement(training_times3)
print(result3)  # Output: None

#CASE 4:
training_times4 = [5, 5, 5, 5, 5]
result4 = find_improvement(training_times4)
print(result4)  # Output: 0

#CASE 5:
training_times5 = [4]
result5 = find_improvement(training_times5)
print(result5)  # Output: None

#CASE 6:
training_times6 = [3, 4, 5, 6, 7, 8, 9, 8, 9, 8, 7, 5, 5, 2, 4, 5, 6, 7, 6]
result6 = find_improvement(training_times6)
print(result6)  # Output: 6


'''
TASK 2
TITLE: Text Transformation - Finding Keywords

PROBLEM STATEMENT: You are developing a data transformation tool for processing text data. Your task is to identify
and transform specific keywords within a text string. To accomplish this, you need to determine if a given keyword
is a substring of the input text and apply the transformation to all occurrences of that keyword.

Function Signature:
def transform_text(input_text: str, keyword: str, transformation: str) -> str:
    pass

INPUT: input_text: A string containing the input text data (length ≤ 10^4 characters).
keyword: A string representing the keyword to be found and transformed (length ≤ 100 characters).
transformation: A string representing the transformation to be applied to occurrences of the keyword (length ≤ 100 characters).

OUTPUT: A string representing the transformed text data after applying the specified transformation to all
occurrences of the keyword.

Notes:
In each example, the transform_text function should find all occurrences of the specified keyword within the
input_text and replace them with the transformation string.
'''
def transform_text(input_text: str, keyword: str, transformation: str) -> str:

  #checking for empty list
  if len(input_text) == 0 or len(keyword) == 0 or len(transformation) == 0:
        return None

  #checking the length of each string passed as parameter
  if len(input_text) > 10000 or len(keyword) > 100 or len(transformation) > 100:
    return None

  #split the sentence into a list of words
  split_input_text = input_text.split()

  #loop through the indexes of the words
  for index in range(len(split_input_text) - 1):
    if split_input_text[index] == keyword: #compare word at each index to the keyword
      split_input_text.remove(split_input_text[index]) #if word is the same as keyword, remove word
      split_input_text.insert(index, transformation) #insert transformation word at the index of the removed word

  #transform words back to a sentence
  transformed_text = " ".join(split_input_text)

  return transformed_text


#Example 1:
input_text = "The quick brown fox jumps over the lazy dog."
keyword = "fox"
transformation = "cat"
result = transform_text(input_text, keyword, transformation)
print(result)
#Output: "The quick brown cat jumps over the lazy dog."

#Example 2:
input_text = "Python is a popular programming language. Python is versatile and easy to learn."
keyword = "Python"
transformation = "Java"
result = transform_text(input_text, keyword, transformation)
print(result)
#Output: "Java is a popular programming language. Java is versatile and easy to learn."