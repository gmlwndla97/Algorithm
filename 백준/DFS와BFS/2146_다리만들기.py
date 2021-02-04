import sys
from collections import deque


n=int(sys.stdin.readline().rstrip())
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
cnt=1
visit=[[0] *n for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
minval=987654321
bridge=[]
answer=987654321
def dfs(x, y, num):
    visit[x][y]=1
    arr[x][y]=num
    for i in range(0, 4):
        nx=dx[i]+x
        ny=dy[i]+y
        if(nx>=0 and nx<n and ny>=0 and ny<n):
            if(visit[nx][ny]==0 and arr[nx][ny]==1):
                dfs(nx, ny, num)

"""
5
1 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 0 0 1
"""


def bfs(k):
    while(q):
        now_x=q[0][0]
        now_y=q[0][1]
        q.popleft()


        for i in range(0, 4):
            nx=dx[i]+now_x
            ny=dy[i]+now_y
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if arr[nx][ny]==0 and visit[nx][ny]==0:
                    dist[nx][ny] = dist[now_x][now_y] + 1
                    visit[nx][ny]=1
                    q.append((nx, ny))

                if arr[nx][ny] != k and arr[nx][ny] != 0:
                    print(answer)
                    answer = dist[now_x][now_y]
                    return



for i in range(0, n):
    for j in range(0, n):
        if(arr[i][j]==1 and visit[i][j]==0):
            dfs(i, j, cnt)
            cnt+=1


q=deque()
visit=[[0] *n for _ in range(n)]
dist=[[0] *n for _ in range(n)]

for k in range(1, cnt):
    for i in range(0, n):
        for j in range(0, n):
         if arr[i][j]==k and visit[i][j]==0:
             q.append((i, j))
             visit[i][j]==1

    bfs(k)
   # print(answer)
    answer=min(minval, answer)
    minval=987654321
    visit = [[0] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    q=deque()
print(answer)

