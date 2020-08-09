def dfs(v):
    print(v,end=' ')
    visit[v]=1
    for i in range(1,n+1):
        if arr[v][i]==1 and visit[i]==0:
            dfs(i)



def bfs(v):
    queue.append(v)
    visit[v] = 1
    while queue:
        first=queue[0]
        queue.popleft()
        print(first, end=' ')
        for i in range(1, n+1):
            if arr[first][i]==1 and visit[i]==0:
                queue.append(i)
                visit[i]=1


n,m,v=map(int, input().split())
arr=[[0]*(n+1) for _ in range(n+1)]
visit=[0]*(n+1)
for i in range(0,m):
    x,y=map(int,input().split())
    arr[x][y]=1
    arr[y][x]=1


dfs(v)
from collections import deque
queue = deque()
for i in range(1, n + 1):
    visit[i] = 0
print()
bfs(v)
