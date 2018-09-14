# Making Python Lists #########################################

a_list = [1, 2, 'a', 3.14159]
week_days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
list_of_lists = [ [1, 2, 3], ['a', 'b', 'c'] ]
list_from_collection = list('Hello')

#print(a_list)
#print(week_days_list)
#print(list_of_lists)
#print(list_from_collection)
#print([])


# List of Lists #####################################################
spreadsheet_list = [ ['Name', 'Age', 'GPA'], ['Bill', 25, 3.55], ['Rich', 26, 4.00] ]
row = spreadsheet_list[1]
#print(row)

column = row[2]
#print(column)
#print(spreadsheet_list[1][2])


# Indexing and Slicing ###############################################
my_list = [1, 'a', 3.14159, True]
#print(my_list[1])
#print(my_list[-1])
#print(my_list[:])
#print(my_list[:3:2])
#print(my_list[::2])
#print(my_list[2:])
#print(my_list[:3])
#print(my_list[10]) #gives IndexError


# Operators ##########################################################
my_list = [1, 2, 3]
your_list = ['a', 'b', 'c']
concat_list = my_list + your_list
rep_list = my_list * 3

#print(concat_list)
#print(rep_list)

#print([1, 2, 3, 4] < [1, 2, 3, 0])
#print([1, 2, 3, 4] < [1, 2, 3, 4, 0])

#print(1 in my_list)
#print(1 in your_list)

#print([1, 2, 'one', 'two'] < [3, 4, 5, 6])
#print([1, 2, 'one', 'two'] < [1, 2, 5, 6]) #TypeError: '<' not supported between instances of 'str' and 'int'


# Functions ##########################################################
# len, min, max, sum

int_list = [1, 2, 3, 4, 5]
float_list = [1.0, 2.0, 3.0, 4.0, 5.0]
str_list =  ['a', 'b', 'c', 'd', 'e']
nested_list = [int_list, float_list, str_list]

#print(len(int_list))
#print(len(nested_list))
#print(min(float_list))
#print(min(str_list))
#print(max(str_list))
#print(sum(int_list))
#print(sum(str_list)) #TypeError: unsupported operand type(s) for +: 'int' and 'str'


# List Iteration ######################################################
my_list = [1, 3, 4, 8]
for element in my_list:
    continue #erase this!
    print(element, end = ' ')

# Lists are Mutable ###################################################
my_list = [1, 2, 'a', 'z']
#print(my_list)

#my_list[0] = True
#print(my_list)

#my_list[-1] = 7
#print(my_list)

#my_list[:2] = [27]
#print(my_list)

#my_list[:] = [1, 2, 3, 4]
#print(my_list)

#my_list[2:]  = 'abc'
#print(my_list)

#my_list[:2] = 15 #TypeError: can only assign an iterable

# List Methods #########################################################
# index, count, append, pop, extend, insert, remove, sort, reverse

#a_list = [1, 12, 5, 8]

#a_list.append(17)
#print(a_list)

#a_list.append([40, 50, 60])
#print(a_list)

#another_list = [20, 2]
#a_list.extend(another_list)
#print(a_list)

#a_list.insert(3, 30)
#print(a_list)

#a_list.remove(8) #first occurance
#print(a_list)

#print(a_list.pop()) #pop last element of list and returns it
#print(a_list)

#print(a_list.index(17))
#print(a_list.count(5))

#a_list.remove([40, 50, 60])
#a_list.sort()
#print(a_list)

#a_list.reverse()
#print(a_list)

# Split / Multiple ####################################################
result = 'this is a test'.split()
#print(result)

result = 'field1,field2,field3,field4'.split(',')
#print(result)

element1, element2, element3 = [1, 2, 3]
#print(element1)
#print(element2)
#print(element3)

field1, field2, field3 = 'Python is great'.split()
#print(field1)
#print(field2)
#print(field3)

# Match the number of the elements to unpack!

#element1, element2 = [1, 2, 3] #ValueError: too many values to unpack
#element1, element2, element3 = [1, 2] #ValueError: not enough values to unpack


# Sorted Function ####################################################
# Sorted function returns the sorted list or string, without changing the original one.

my_list = [27, 56, 4, 18]
sorted_list = sorted(my_list)
#print(sorted_list, my_list)

my_str = "Hi mom"
sorted_str = sorted(my_str)
#print(sorted_str, my_str)

