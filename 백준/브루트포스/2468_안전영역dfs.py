import sys
from collections import deque
sys.setrecursionlimit(15000)
n=int(sys.stdin.readline().rstrip())
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
#temp=[[0]*n for _ in range(n)]
cnt=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
def dfs(x, y, nn):
    for i in range(0, 4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if(visit[nx][ny]==0 and arr[nx][ny]>nn):
                visit[nx][ny]=1
                dfs(nx, ny,nn)


for number in range(max(map(max, arr))):
    land=0
    visit = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if visit[i][j]==0 and arr[i][j]>number:
                visit[i][j]=1
                dfs(i, j, number)
                land+=1
    if land>cnt:
        cnt=land


print(cnt)