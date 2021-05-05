import sys
from collections import deque
n, m, k, x=map(int, sys.stdin.readline().rstrip().split())
arr=[[] for _ in range(n+1)]
q=deque()
visit=[0]*(n+1)
for _ in range(m):
    a, b=map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)


q.append((x,0))
visit[x]=1
ans=[]
while q:
    now=q[0][0]
    cnt=q[0][1]
   # print(now, cnt)
    if(cnt==k):
        ans.append(now)
    q.popleft()
    for i in range(0, len(arr[now])):
        if(visit[arr[now][i]]==0):
           # print(arr[now][i], cnt+1)
            visit[arr[now][i]]=1
            q.append((arr[now][i], cnt+1))


if(len(ans)==0):
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)