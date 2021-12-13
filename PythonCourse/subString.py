s = "1102021222"
k = 2
res = 0
for i in range(len(s)):
    count = 0
    for j in range(k,len(s)):
        string = s[i:j]
        l = set(string)
        for value in l:
            if(string.count(value)==2):
                count+=1
    if(count>1):
        res +=1
print(res)