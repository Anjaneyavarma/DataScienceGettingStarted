digits=[1,2,3,9]
digits[-1] = digits[-1] + 1
l = []
if(digits[-1]>=10):
    string = str(digits[-1])
    for i in range(len(string)):
        l.append(int(string[i]))
digits[-1] = l
print(digits)