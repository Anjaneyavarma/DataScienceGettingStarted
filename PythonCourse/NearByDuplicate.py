nums=[1]
res = 0
l = []
k=1
if(len(nums)<=1):
    print("true")
for i in range(0,len(nums)):
    for j in range(i+1, len(nums)):
        if(nums[i]==nums[j]):
            res = abs(i-j)
            l.append(res)
print(l)
print(max(l))
if(max(l)<=k):
    print("true")
else:
    print("false")