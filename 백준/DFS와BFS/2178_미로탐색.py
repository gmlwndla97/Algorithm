import sys
from collections import deque
q=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n, m= map(int, sys.stdin.readline().rstrip().split())
arr=[list(map(int, input())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]

cnt=0
visit[0][0]=1
q.append((0, 0, 0))
while q:
    front_x, front_y, cnt=q[0]
    q.popleft()
    if front_x==n-1 and front_y==m-1:
        print(cnt+1)
    else:
        for i in range(0,4):
            nx=dx[i]+front_x
            ny=dy[i]+front_y
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if arr[nx][ny]==1 and visit[nx][ny]==0:
                    visit[nx][ny]=1
                    newcnt=cnt+1
                    q.append((nx, ny, newcnt))
