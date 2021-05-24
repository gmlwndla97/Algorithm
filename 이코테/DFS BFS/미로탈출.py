import sys
from collections import deque
q=deque()
n, m=map(int, sys.stdin.readline().rstrip().split())
arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

q.append((0, 0, 1))
while(q):
    x, y, cnt=q[0]
    q.popleft()
    print(x, y, cnt)
    if(x==n-1 and y==m-1):
        break
    for i in range(0, 4):
        nx=dx[i]+x
        ny=dy[i]+y
        if(nx>=0 and nx<n and ny>=0 and ny<m):
            if(arr[nx][ny]==1 and visit[nx][ny]==0):
                visit[nx][ny]=1
                q.append((nx, ny, cnt+1))


