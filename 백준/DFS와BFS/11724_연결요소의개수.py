import sys
from collections import deque
q=deque()
n,m=map(int,sys.stdin.readline().rstrip().split())
visit=[0]*(n+1)
arr=[[0]*(n+1) for _ in range(n+1)]


def bfs(x):
    q.append(x)
    visit[x]=1
    while q:
        front=q[0]
        q.popleft()
        for i in range(1, n+1):
            if arr[front][i]==1 and visit[i]==0:
                q.append(i)
                visit[i]=1



list=[]
for i in range(0, m):
    x, y=map(int,sys.stdin.readline().rstrip().split())
    arr[x][y]=1
    arr[y][x]=1

cnt=0
for i in range(1, n+1):
    if visit[i]==0:
        bfs(i)
        cnt=cnt+1
        list.append(cnt)

print(len(list))

