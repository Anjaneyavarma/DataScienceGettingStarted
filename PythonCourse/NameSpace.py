# here "a" is initialized with the value, which is stored in the memory, the id is
a = 2
print(id(2),"+", id(a))

#here the "a" is changed, so for the value of the a has different memory location
a = a+1
print("\n", id(a))

# This is efficient as Python does not have to create a new duplicate object.
# This dynamic nature of name binding makes Python powerful; a name could refer to any type of object.

#"b" is assigned same as vlue of "a", since the b takes the memory of the "a" having value 2, new memory is not created
b = 2
print("\n",id(b))