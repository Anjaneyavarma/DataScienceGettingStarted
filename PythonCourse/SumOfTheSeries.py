a = int(input())
b = int(input())
l = []
odd_number = 1
sum=0
for i in range(b):
    power = a**odd_number
    l.append(power)
    odd_number +=2
for i in range(len(l)):
    if(i%2==0):
        sum+=l[i]
    else:
        sum-=l[i]

print(sum)
