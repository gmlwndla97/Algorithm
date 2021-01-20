from collections import  deque

q=deque()

numbers=[6, 10, 2]
#numbers=[3, 30, 34, 5, 9]
temp=list(map(str, numbers))
maxlen=0

for i in temp:
    if len(i)>maxlen:
        maxlen=len(i)

#이제 maxlen=2가 되었음.
#이제 나머지 애들을 2자리로 늘려줘야함
map={}

for i in range(0, len(temp)):
    if len(temp[i])<maxlen:
        length=len(temp[i])
        strr=''
        for k in range(length, maxlen):
            strr+=temp[i][length-1]
            #print(str)

        temp[i]+=strr
    tempnum=int(temp[i])

    map[i]=tempnum


newmap=sorted(map.items(), key=lambda x:x[1], reverse=True)
answer=''
for i in newmap:
    q.append(i)

for i in q:
    index, value=i
    answer+=str(numbers[index])

print(answer)