import sys
n=int(sys.stdin.readline().rstrip())
num=[0]*(n+1)
visit=[0]*(n+1)
head=0
queue=[]
def dfs(index):
    if(visit[index]==0):
        visit[index]=1
        dfs(num[index])
    else:
        #이미 visit이 되어있었단 뜻이지.
        #그럼 처음에 들어온 head와 같은지 보면 사이클
        global head
        if(index==head):
            #이 경우에는 자기로 시작해서 자기자신으로 돌아온다는뜻
            #자기번호만 답에 추가해줌.
            queue.append(index)
            return 1
        else:

            return 0



for i in range(1, n+1):
    x=int(sys.stdin.readline().rstrip())
    num[i]=x

for i in range(1, n+1):
    head = i
    dfs(i)
    visit=[0]*(n+1)



print(len(queue))
queue.sort()
for i in queue:
    print(i)