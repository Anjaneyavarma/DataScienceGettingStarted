import math
a = int(input())
b = int(input())
count = 0
for i in range(a,b+1):
    sqrt = i**0.5
    if(sqrt==math.ceil(sqrt)):
        count+=1
print(count)