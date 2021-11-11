a = int(input())
for i in range(a):
    left_space = "  "*i
    right_space = (a - i - 2)
    if (i == 0):
        for j in range(a):
            print("*", end=" ")
        print()
    else:
        if right_space>=0:
            print(left_space + "* " + "  "*right_space + "*")
        else:
            print(left_space + "*")


