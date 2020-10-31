import sys
from string import ascii_uppercase
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x, y, cnt):
    global maxval
    maxval=max(cnt, maxval)

    for i in range(0, 4):
        nx=dx[i]+x
        ny=dy[i]+y
        if(nx>=0 and nx<r and ny>=0 and ny<c):
            if(alpha[ord(arr[nx][ny])-65]==0):
                alpha[ord(arr[nx][ny])-65]=1
                dfs(nx, ny, cnt+1)
                alpha[ord(arr[nx][ny]) - 65] = 0

    return


r, c= map(int, sys.stdin.readline().rstrip().split(' '))
arr=[list(sys.stdin.readline().rstrip()) for _ in range(r)]
visit=[[0]*(r) for _ in range(c)]
alpha=[0]*26
maxval=0
visit[0][0] = 1
alpha[ord(arr[0][0])-65]=1
dfs(0, 0, 1)

print(maxval)