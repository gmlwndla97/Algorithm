import sys
com=int(input())
line=int(input())
arr=[[0]*(com+1) for _ in range(com+1)]
visit=[0]*(com+1)
for i in range(0, line):
    x, y= map(int, input().split())
    arr[x][y]=1
    arr[y][x]=1

from collections import deque
q =deque()
cnt=0
q.append(1)
visit[1]=1

while q:
    front=q[0]
    q.popleft()
    for i in range(1, com+1):
        if arr[front][i]==1 and visit[i]==0:
            visit[i]=1
            q.append(i)
            cnt=cnt+1

print(cnt)

