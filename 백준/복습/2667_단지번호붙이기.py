import sys
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n=int(sys.stdin.readline().rstrip())
cnt=0

def dfs(x, y):
    visit[x][y]=1
    #arr[x][y]=cnt
    #print(cnt)
    global cnt
    cnt+=1
    for i in range(0, 4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if visit[nx][ny]==0 and arr[nx][ny]==1:
                dfs(nx, ny)

arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visit=[[0]*n for _ in range(n)]
ans=[]
for i in range(0, n):
    for j in range(0, n):
        if visit[i][j]==0 and arr[i][j]==1:
            cnt=0
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
ans.sort()
for i in ans:
    print(i)
