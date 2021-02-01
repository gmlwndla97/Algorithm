import sys
from collections import deque

n, m, v=map(int, sys.stdin.readline().rstrip().split(' '))
visit=[0]*(n+1)
arr=[[0]*(n+1) for _ in range (n+1)]
ans=[]
q=deque()
def dfs(start):
    visit[start]=1
    ans.append(start)
    for i in range(1, n+1):
        if arr[start][i]==1 and visit[i]==0:
            dfs(i)


def bfs(start):
    q.append(start)
    visit[start]=1
    while(q):
        now=q[0]
        ans.append(now)
        q.popleft()
        for i in range(1, n+1):
            if arr[now][i]==1 and visit[i]==0:
                visit[i]=1
                q.append(i)


for _ in range(0, m):
    x, y= map(int, sys.stdin.readline().rstrip().split())
    arr[x][y]=1
    arr[y][x]=1

dfs(v)
for i in ans:
    print(i, end=' ')
visit=[0]*(n+1)
ans=[]
bfs(v)
print()
for i in ans:
    print(i, end=' ')