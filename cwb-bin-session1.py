'''
SESSION 1 (07/08/2023)
Mentor and Facilitator ==> ANDY AFFUL

Write a program that given list of words and a positive integer value 'n', finds the words that are longer than n from a given list of words.
 - ALGORITHM
- Create an empty list, l
- Loop through the list
- Get the len of each word, s and compare to 'n'
- Add s if len > n
- Return list l
'''

# Solution to First Session Task
def word_length_finder(word_list, length):
    # declare an empty list variable to hold new words longer than specified length
    new_word_list = list()

    # declare a variable that holds the length of the word_list
    word_list_length = len(word_list)

    # return empty list if word list is empty
    if word_list_length == 0:
        # ---->>>> Your function should return a list so if 'word_list_length' is 0, then you have to return an empty list 'new_word_list'
        return new_word_list

    #using list comprehension
    # new_word_list = [word for word in word_list if len(word) > length]

    # looping through the word list and checking the length of word against the specified length
    for word in word_list:
        word_length = len(word)
        if word_length > length:
            new_word_list.append(word)

    return new_word_list


#TEST CASES
list_of_words = []
list_of_words1 = ["man"]
list_of_words2 = ["man", "go", "tense"]
list_of_words3 = [
    "man", "many", "orange", "hall", "callous",
    "viral", "native", "bulb", "tense", "island",
    "meal", "top", "dashing", "needless", "ear"
    ]

#Test with an empty list
print(word_length_finder(list_of_words, 3))
