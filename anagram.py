# 1. Anagrams ####################################################

# Words are anagrams if they use a different arrangement of the same set of letters to form words
# ex) cinema / iceman

# Algorithm
#
#   0. Get the input from keyboard, slice the string into two words.

#   1. (Function) Input two words to examine.
#   2. Sort the letters of each word into a new string.
#   3. Compare the sorted string.

# Pseudocode

#   function are_anagram(word1: str, word2: str):
#       if sorted(word1) == sorted(word2):
#           return True
#       else:
#           return False


# Code

# 0. Get the input from keyboard, slice the string into two words.
print("Anagram Test")
two_words = input("Enter two space seperated words: ")
two_word_list = two_words.split()
word1 = two_word_list[0]
word2 = two_word_list[1]

# 1. (Function) Input two words to examine.
def are_anagrams(word1, word2):

# 2. Sort the letters of each word into a new string.
    word1_sorted = sorted(word1) #sorted function 'returns' the list!
    word2_sorted = sorted(word2)

# 3. Compare the sorted string.
    if word1_sorted == word2_sorted:
        print("The words are anagrams.")
        return True
    else:
        print("The words are not anagrams.")
        return False

# 4. Run the function
are_anagrams(word1, word2)

"""
# Additional Implementation: Exception handling
# Checking errors of the input

def are_anagrams_return(word1, word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    return word1_sorted == word2_sorted

# Checking errors of the input
valid_input_bool = False
while not valid_input_bool:
    try:
        two_words = input("Enter two space seperated words: ")
        word1, word2 = two_words.split()
        valid_input_bool = True

    except ValueError:
        print('Bad Input')

if are_anagrams_return(word1, word2):
    print("The words {} and {} are anagrams.".format(word1, word2))
else:
    print("The words {} and {} are not anagrams.".format(word1, word2))

"""




