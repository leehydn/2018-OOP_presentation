# 1. Mutable object and Immutable object

    # Immutable object: could not change the value after the declaration
    # ex. Number(int, float), string, tuple

    # Mutable object: could change the value after the declaration
    # ex. list, dictionary

# 2. Object and Value
# '==': True if the 'value' is same
# 'is': True if the 'object' is same (whether they have same reference or not)
# function id(): returns the 'identity' or 'address' of

list1 = [1, 2, 3]
list2 = [1, 2, 3]

#print(list1 == list2) #True
#print(list1 is list2) #False
#print(id(list1), id(list2))

# 3. Copy by substitution, Shallow copy, Deep copy

a_list = [1, 2, 3]
b_list = [5, 6, 7]
a_list.append(b_list)

#print(a_list)

c_list = b_list #another name of [5, 6, 7], which b_list was originally pointing at
#print(c_list)

c_list[2] = 88
#print("c_list:", c_list, ',', "b_list:", b_list)

#print(a_list) 

import copy

a_list = [1, 2, 3]
b_list = [5, 6, 7]
a_list.append(b_list)

c_list = copy.deepcopy(a_list)
b_list[0] = 1000
#print(a_list)

#print(c_list)