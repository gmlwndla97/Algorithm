import sys
from collections import deque
q=deque()

def dfs(idx, length):
    if length==m:
        for i in range(0, len(q)):
            print(q[i], end=' ')
        print()
        return

    else:
        for i in range(idx, n+1):
            q.append(i)
            dfs(i, length+1)
            q.pop()


n, m=map(int, sys.stdin.readline().rstrip().split())
dfs(1, 0)