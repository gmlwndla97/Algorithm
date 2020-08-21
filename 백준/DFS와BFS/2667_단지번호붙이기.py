import sys
from collections import deque
q=deque()
cnt=0#단지 내 집의 수
num=[]

def dfs(x, y, cnt):
    now_x = x
    now_y = y
    visit[now_x][now_y]=1
    num[cnt]=num[cnt]+1
    for i in range(0, 4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if arr[nx][ny] == 1 and visit[nx][ny] == 0:
                dfs(nx, ny, cnt)



dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
n=int(input())
arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visit=[[0]*(n+1) for _ in range(n+1)]
cntarr=[0]*(n*n)


housecount=0 #단지 수
for i in range(0, n):
    for j in range(0, n):
        if arr[i][j]==1 and visit[i][j]==0:
            housecount=housecount+1
            num.append(0)
            dfs(i,j,cnt)
            #print(cnt)
            cnt=cnt+1

print(housecount)
num.sort()
for i in num:
    print(i)



