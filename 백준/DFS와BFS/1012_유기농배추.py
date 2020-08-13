import sys
sys.setrecursionlimit(10**8)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x, y):
    visit[x][y]=1
    for i in range(0,4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if visit[nx][ny]==0 and arr[nx][ny]==1:
                dfs(nx, ny)


        

t=int(input())
for i in range(0, t):
    m,n,k=map(int, sys.stdin.readline().rstrip().split())
    arr=[[0]*(m) for _ in range(n)]
    visit=[[0]*(m) for _ in range(n)]

    for i in range(0, k):
        x, y=map(int, sys.stdin.readline().rstrip().split())
        arr[y][x]=1

    #print(arr)
    cnt=0
    list=[]
    for i in range(0, n):
        for j in range(0, m):
            if arr[i][j]==1 and visit[i][j]==0:
                dfs(i,j)
                cnt=cnt+1
                list.append(cnt)

    print(len(list))