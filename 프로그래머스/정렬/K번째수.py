array=[1,5,2,6,3,7]
commands=[[2,5,3],[4,4,1],[1,7,3]]
list=[]
for i in range(0, len(commands)):
    temp = commands[i]
    start=temp[0]
    end=temp[1]
    rank=temp[2]
    newArr=array[start-1:end]
    newArr.sort()
    list.append(newArr[rank-1])
print(list)