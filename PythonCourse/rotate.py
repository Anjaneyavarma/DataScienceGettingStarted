nums = [1,2,3,4,5,6,7]
k=3
if(k>len(nums)):
    k = k- len(nums)
for i in range(0,k+1):
    temp = nums[0]
    for j in range(1,len(nums)):
        nums[j-1] = nums[j]
    nums[len(nums)-1] = temp
print(nums)