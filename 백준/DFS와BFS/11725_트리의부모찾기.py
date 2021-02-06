import sys
from collections import deque

q=deque()
n=int(sys.stdin.readline().rstrip())
arr=[[] for i in range(n+1)]
parent=[0 for _ in range(n+1)]

def bfs():
    while(q):
        start=q[0]
       # print(start)
        q.popleft()
        for i in range(0, len(arr[start])):
            if arr[start][i]!=1 and parent[arr[start][i]]==0:
                parent[arr[start][i]]=start
                q.append(arr[start][i])
                #print("append:", arr[start][i])
                #print(parent)



for _ in range(1, n):
    x, y= map(int, sys.stdin.readline().rstrip().split())
    arr[x].append(y)
    arr[y].append(x)

parent[1]=-1

for i in range(0, len(arr[1])):
    parent[arr[1][i]]=1
    q.append(arr[1][i])
    bfs()

for i in range(2, n+1):
    print(parent[i])