# 2. File Analysis ####################################################
gba_file = open("./OOP-master/lincoln.txt", "r")

#   1. Length of Gettysburg Address ###################################
def make_word_list_1(a_file):
    word_list = []

    for line_str in a_file:
        line_list = line_str.split()
        word_list.extend(line_list)
    
    return word_list

#speech_list = make_word_list_1(gba_file)
#print(speech_list)
#print("Length:", len(speech_list)) #Length: 271

#   2. List without non-word '--' #####################################
def make_word_list_2(a_file):
    word_list = []

    for line_str in a_file:
        line_list = line_str.split()
        for word in line_list:
            if word != "--":
                word_list.append(word)

    return word_list

#speech_list = make_word_list_2(gba_file)
#print(speech_list)
#print("Length:", len(speech_list))

#   3. List of unique words ###########################################
def make_unique(word_list):
    unique_list = []
    for word in word_list: 
        if word not in unique_list:
            unique_list.append(word)

    return unique_list

#speech_list = make_word_list_2(gba_file)
#print(speech_list)
#print("Speech Length:", len(speech_list))
#print("Unique Length:", len(make_unique(speech_list)))

#   4. Additional Implements ###########################################
#       1. Different capitalization
#       2. Different surrounding punctuation

def make_word_list_3(a_file):
    word_list = []

    for line_str in a_file:
        line_list = line_str.split()
        for word in line_list:
            word = word.lower() #Compare words only in lower case!
            word = word.strip('.,') #Get rid of punctuation marks!
            if word != "--": #Get rid of non-word "--" 
                word_list.append(word)
    return word_list

#speech_list = make_word_list_3(gba_file)
#print("Speech Length:", len(speech_list))
#unique_list = make_unique(speech_list)
#print(unique_list)
#print("Unique length:", len(make_unique(unique_list)))
