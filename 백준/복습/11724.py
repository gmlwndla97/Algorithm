import sys
n, m=map(int, sys.stdin.readline().rstrip().split())
arr=[[0]*(n+1) for _ in range(n+1)]
visit=[0]*(n+1)
count=0
def dfs(start):
    visit[start]=1
    for i in range(1, n+1):
        if(arr[start][i]==1 and visit[i]==0):
            dfs(i)


for _ in range(m):
    x, y=map(int, sys.stdin.readline().rstrip().split())
    arr[x][y]=1
    arr[y][x]=1



for i in range(1, n+1):
    if(visit[i]==0):
        dfs(i)
        count+=1

print(count)