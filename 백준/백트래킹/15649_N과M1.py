import sys
from collections import deque

q=deque()
result=deque()


def dfs(now,length):
    if length==m:
        for i in range(0, len(result)):
            print(result[i], end=' ')
        print()
        return
    else:
        for i in range(1, n+1):
            if visit[i]==0:
                result.append(i)
                visit[i]=1
                dfs(i+1, length+1)
                result.pop()
                visit[i]=0


n,m=map(int, sys.stdin.readline().rstrip().split())
visit=[0]*(n+1)
dfs(1, 0)
