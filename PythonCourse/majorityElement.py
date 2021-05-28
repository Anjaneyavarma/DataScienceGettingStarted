nums=[1,2]
l = [a for a in set(nums) if nums.count(a)>len(nums)//3]
print(l)