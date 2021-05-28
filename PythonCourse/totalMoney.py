count = 0
sum=0
init=1
days=1
n = 30
while(days<=n):
    sum = sum + init + count
    init += 1
    if(days%7==0):
        init=1
        count+=1
    days+=1

print(sum)



