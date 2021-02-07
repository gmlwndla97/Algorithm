import sys
from collections import deque

q=deque()
m, n=map(int, sys.stdin.readline().rstrip().split())
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
maxday=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(0, n):
    for j in range(0, m):
        if arr[i][j] == 1:
            visit[i][j] = 1
            q.append((i, j, 0))

while (q):
    now_x = q[0][0]
    now_y = q[0][1]
    now_cnt = q[0][2]
    maxday = max(maxday, now_cnt)
    q.popleft()
    for i in range(0, 4):
        nx = dx[i] + now_x
        ny = dy[i] + now_y
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if arr[nx][ny] == 0 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                arr[nx][ny] = now_cnt + 1
                q.append((nx, ny, now_cnt + 1))

#print(arr)

for i in arr:
    if 0 in i:
        print(-1)
        sys.exit(0)

print(maxday)


