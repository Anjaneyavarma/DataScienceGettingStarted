# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed data types
my_list = [1, "Hello", 3.4]
print(my_list[0])

# nested list, negative indexing
my_list = ["mouse", [8, 4, 6], ['a']]
print(my_list[-2][2])

# Nested List, Nested indexing
n_list = ["Happy", [2, 0, 1, 5]]
print(n_list[0][1])

# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]
print(odd)

# Appending and Extending lists in Python
odd = [1, 3, 5]
odd.append(7)
print(odd)
odd.extend([9, 11, 13])
print(odd)

# Concatenating and repeating lists
odd = [1, 3, 5]
print(odd + [9, 7, 5])
print(["re"] * 3)

#inserting elements
odd =[1,9]
odd.insert(1,3)
print(odd)

odd[2:2] = [5,7]
print(odd)

# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]
print(my_list)

# delete multiple items
del my_list[1:5]
print(my_list)

# delete entire list
del my_list