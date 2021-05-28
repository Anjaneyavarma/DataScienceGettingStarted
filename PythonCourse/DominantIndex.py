nums=[3,6,1,0]
max1 = -1
max2 = -1
if(len(nums)==1):
    print(-1)
for i in range(len(nums)):
    if nums[i] > max1:
        max2=max1
        max1=nums[i]
    if max2<nums[i] and max1>nums[i]:
        max2=nums[i]
if(max1>=(max2*2)):
    print(nums.index(max1))
else:
    print(-1)