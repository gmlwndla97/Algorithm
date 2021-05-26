import sys
from collections import deque

q=deque()
n, m, k, x=map(int,sys.stdin.readline().rstrip().split())
graph=[[] for _ in range(n+1)]
visit=[0]*(n+1)
for _ in range(m):
    a, b=map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)

q.append((x, 0))
visit[x]=1
answer=[]
while(q):
    node, depth=q[0]
    if(depth==k):
        answer.append(node)
    q.popleft()
    for i in graph[node]:
        if(visit[i]==0):
            visit[i]=1
            q.append((i, depth+1))

if(len(answer)==0):
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)