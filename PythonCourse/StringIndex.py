name = "John walker"
print(name[0])
print(name[-1])
print(name[1:3])
print(name[:5] + name[5:])

# python string's are immutable
# If you need a different string, you should create a new on
print('z' + name[1:])

print(len(name))

for i in range(1, len(name)+1):
    print(name[i-1], end=" ")

print()

for i in range(1, len(name)+1):
    print(name[-i], end=" ")