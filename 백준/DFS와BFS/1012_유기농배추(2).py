import sys
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]


q=deque()

def bfs(x, y):
    q.append((x,y))
    visit[x][y]=1
    while q:
        front_x, front_y = q[0]
        q.popleft()
        for i in range(0, 4):
            nx=dx[i]+front_x
            ny=dy[i]+front_y
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visit[nx][ny] == 0 and arr[nx][ny] == 1:
                    visit[nx][ny]=1
                    q.append((nx,ny))




t=int(input())
for i in range(0, t):
    cnt = 0
    list = []
    m,n,k=map(int, sys.stdin.readline().rstrip().split())
    arr=[[0]*(m) for _ in range(n)]
    visit=[[0]*(m) for _ in range(n)]

    for i in range(0, k):
        x, y=map(int, sys.stdin.readline().rstrip().split())
        arr[y][x]=1

    for i in range(0, n):
        for j in range(0, m):
            if arr[i][j]==1 and visit[i][j]==0:
                bfs(i,j)
                cnt=cnt+1
                list.append(cnt)

    print(len(list))