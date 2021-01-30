import sys
from collections import deque

n,m =map(int, sys.stdin.readline().rstrip().split())
visit=[0]*(n+1)
arr=[[0] * (n+1) for _ in range(n+1)]
q=deque()
cnt=0

for i in range(0, m):
    a, b=map(int, sys.stdin.readline().rstrip().split())
    arr[a][b]=1
    arr[b][a]=1

for i in range(1, n+1):
    if visit[i]==0:
        cnt += 1
        q.append(i)
        visit[i]=1
        while(q):
            front=q[0]
            q.popleft()
            for j in range(1, n+1):
                if arr[front][j]==1 and visit[j]==0:
                    visit[j]=1
                    q.append(j)


print(cnt)
