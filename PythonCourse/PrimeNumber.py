m = int(input("Enter a Starting No: "))
n = int(input("Enter a Ending No: "))
count = 0
for i in range(m,n):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break;
        else:
            print(i,end=", ")
            count+=1
print()
print("count: ",count)