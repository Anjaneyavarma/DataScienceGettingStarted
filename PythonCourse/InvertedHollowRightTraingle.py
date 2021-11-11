a = int(input())

for i in range(a):
    right_space = i-1
    left_space = a-i-1
    if(i == a-1):
        for j in range(a):
            print("*",end=" ")
    else:
        if(left_space==a-1):
            print("  "*left_space+"*")
        else:
            print("  "*left_space+"* "+"  "*right_space+"*")

