import sys
from collections import deque
def dfs(idx, length):
    if length==m:
        for i in range(1, len(visit)):
            if visit[i]==1:
                print(i,end=' ')
        print()
        return
    else:
        for i in range(idx, n+1):
            visit[i]=1
            dfs(i+1, length+1)
            visit[i]=0


n, m=map(int, sys.stdin.readline().rstrip().split())
visit=[0]*(n+1)
dfs(1, 0)