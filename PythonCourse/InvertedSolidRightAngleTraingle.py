a = int(input())

for i in range(a):
    stars = a-i
    left_space = i
    print("  "*left_space+"* "*stars,end=" ")
    print()