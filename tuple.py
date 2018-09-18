#Codes for testing tuple, you can modify

tup = 2, 3
print(tup)

print((1,), (1))

x, y = 'a', 3.14159

my_tuple = 1, 2, 3, 4, 5
print(my_tuple)

print(my_tuple + my_tuple)
print(my_tuple * 3)
print(my_tuple[1])
print(my_tuple[:3])
print(my_tuple[1:3])
print(my_tuple[-1])
print(2 in my_tuple)

for x in my_tuple:
    print(x, end = ' ')

print(len(my_tuple))
print(min(my_tuple))
print(max(my_tuple))
print(sum(my_tuple))
print((1, 2, 3) > (3, 2, 1))