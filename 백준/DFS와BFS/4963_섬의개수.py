import sys
dx=[-1,-1,1,1,0,-1,0,1]
dy=[-1,0,-1,0,-1,1,1,1]
cnt=0

def dfs(x, y, arr, visit):
    visit[x][y]=1
    for i in range(0, 8):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and nx<h and ny>=0 and ny<w:
            if visit[nx][ny]==0 and arr[nx][ny]==1:
                dfs(nx, ny, arr, visit)

while True:
    w, h=map(int, sys.stdin.readline().rstrip().split(' '))
    if w==0 and h==0:
        break
    else:
        arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
        visit=[[0]*w for _ in range(h)]

        cnt=0
        for i in range(0, h):
            for j in range(0, w):
                if arr[i][j] == 1 and visit[i][j] == 0:
                    dfs(i, j, arr, visit)
                    cnt += 1

        print(cnt)
        cnt=0