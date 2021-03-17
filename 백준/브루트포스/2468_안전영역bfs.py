import sys
from collections import deque
sys.setrecursionlimit(100000)
n=int(sys.stdin.readline().rstrip())
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
#temp=[[0]*n for _ in range(n)]
cnt=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()

def bfs(x, y, nn):
    q.append((x,y))
    visit[x][y]=1
    while(q):
        now_x=q[0][0]
        now_y=q[0][1]
        q.popleft()

        for i in range(0, 4):
            nx=dx[i]+now_x
            ny=dy[i]+now_y
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if visit[nx][ny]==0 and arr[nx][ny]>nn:
                    visit[nx][ny]=1
                    q.append((nx, ny))


for number in range(max(map(max, arr))):
    land=0
    visit = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if visit[i][j]==0 and arr[i][j]>number:
                bfs(i, j, number)
                land+=1
    if land>cnt:
        cnt=land


print(cnt)