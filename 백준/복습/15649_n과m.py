import sys
from collections import deque
arr=[]
answer=deque()

n,m=map(int, sys.stdin.readline().rstrip().split())
visit=[0]*n
def dfs(count):
    if(count==m):
        for i in range(0, m):
            print(answer[i], end=' ')
        print()

    for i in range(0, n):
        if(visit[i]==0):
            visit[i]=1
            answer.append(i+1)
            dfs(count+1)
            answer.pop()
            visit[i]=0


dfs(0)

