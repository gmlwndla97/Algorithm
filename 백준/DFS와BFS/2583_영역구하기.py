import sys
from sys import*
setrecursionlimit(10**6)
m, n, k=map(int, sys.stdin.readline().rstrip().split())

def dfs(x, y):
    count = 1
    visit[x][y]=1
    dx=[-1, 1, 0, 0]
    dy=[0,0,-1,1]

    for i in range(0, 4):
        nx=dx[i]+x
        ny=dy[i]+y
        if(nx>=0 and nx<m and ny>=0 and ny<n):
            if (visit[nx][ny]==0):
                if(arr[nx][ny]==0):
                    count+=1
                    dfs(nx, ny)

    clist.append(count)
    return


#좌표 조건이
#일단 둘다 X, Y 순서 바꾸고 행만 M만큼 뺌
#그리고 앞에껀 앞자리 1 뺴고, 뒤에껀 뒷자리 1뺌
#그리고 두 좌표 사이에 해당하는 칸 다 칠함
arr=[[0]*n for _ in range(m)]
visit=[[0]*n for _ in range(m)]
for i in range(0, k):
    lx, ly, rx, ry=map(int, sys.stdin.readline().rstrip().split())
    #순서는 (ly, lx), (ry, rx)
    ly=m-ly
    ry=m-ry
    ly-=1
    rx-=1
    #먼저 x좌표 부터
    for j in range(lx, rx+1):
        arr[ly][j]=1
    #그다음 y좌표
    for j in range(lx, rx+1):
        arr[ry][j]=1

for i in range(0, m):
    for j in range(0, n):
        print(arr[i][j], end='')
    print()

clist=[]
for i in range(0, m):
    for j in range(0, n):
        if(arr[i][j]==0 and visit[i][j]==0):
            dfs(i,j)



print(len(clist))
for i in sorted(clist):
    print(i, end=' ')