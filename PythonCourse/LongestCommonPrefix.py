strs=["ab", "ab"]
res=""
if(len(strs)==1):
    print(strs[0])

for i in range(1,len(strs[0])):
    prefix = strs[0][:i]
    for j in range(len(strs)):
        if (prefix == strs[i][:j]):
            res = prefix

if(len(res)>0):
    print(res)
else:
    print(res)