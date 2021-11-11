a = int(input())

for i in range(a):
    stars = i+1
    left_space = a-i-1
    print("  "*left_space+"* "*stars,end=" ")
    print()