import sys
arr=[]
a, p=sys.stdin.readline().rstrip().split(' ')
arr.append(int(a))
visit=[0]*1000000
answer=[]
answer.append(int(a))
visit[int(a)]=1
num=a
while True:
    temp=0
    for i in num:
        temp+=(pow(int(i), int(p)))
    if visit[temp]==0:
        visit[temp]=1
        answer.append(temp)
    elif visit[temp]==-1:
        break
    else:
        answer.remove(temp)
        visit[temp]=-1
    num=str(temp)
   # print(answer)

print(len(answer))