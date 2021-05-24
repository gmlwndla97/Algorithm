import sys
n, m=map(int,sys.stdin.readline().rstrip().split())
arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
def dfs(x, y):
    visit[x][y]=1
    for i in range(0, 4):
        nx=dx[i]+x
        ny=dy[i]+y
        if(nx>=0 and nx<n and ny>=0 and ny<m):
            if(visit[nx][ny]==0 and arr[nx][ny]==0):
                dfs(nx, ny)

for i in range(0, n):
    for j in range(0, m):
        if(arr[i][j]==0 and visit[i][j]==0):
            dfs(i, j)
            cnt+=1

print(cnt)