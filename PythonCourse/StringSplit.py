sentence = "this problem is an easy problem"
searchWord = "hi"


list = sentence.split()
print(list)

# print(list.index('burger')+1)
# print(type(list[2]))

phrase = sentence.split()
l = len(searchWord)
count=0
for i in range(len(phrase)):
    if(list[i][:l] == searchWord):
        count = i+1
        break
if(count>1):
    print(count)
else:
    print((-1))