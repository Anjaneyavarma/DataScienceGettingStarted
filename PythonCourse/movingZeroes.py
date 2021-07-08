nums = [0,1,0,3,12]
n = len(nums)

nums

for i in range(nums.count(0)):
    nums.append(nums.pop(nums.index(0)))
    nums[:] = nums
print(nums)