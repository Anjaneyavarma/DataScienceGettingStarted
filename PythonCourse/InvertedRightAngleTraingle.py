a = int(input())

for i in range(a+1):
    spaces = a-i
    if(i==0):
        for j in range(a+1):
            print("_",end="")
        print()
    else:
        print("|"+" "*spaces+"/")
