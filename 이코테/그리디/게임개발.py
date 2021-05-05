import sys
n, m=map(int, sys.stdin.readline().rstrip().split())
a, b, dir=map(int, sys.stdin.readline().rstrip().split())
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visit=[[0] * m for _ in range(n)]
dircount=0

dx=[-1,0,1,0]
dy=[0,1,0,-1]
count=1
visit[a][b]=1
while(True):
    newdir=dir-1
    if(newdir==-1): newdir=3

    nx=dx[newdir]+a
    ny=dy[newdir]+b

    if (visit[nx][ny] == 0 and arr[nx][ny] == 0):
        # 회전한다음 왼쪽으로 한칸 전진.
        dir = newdir
        visit[nx][ny] = 1
        a = nx
        b = ny
        count+=1
        dircount = 0
        continue
    else:
        # 회전만 함.
        dir = newdir
        dircount += 1

    if (dircount == 4):
        tempdir = dir + 2
        if (tempdir >= 4):
            tempdir -= 4

        nx = a+dx[tempdir]
        ny = b+dy[tempdir]
        if (arr[nx][ny] == 1):
            break
        else:
            a = nx
            b = ny
            #visit[a][b] = 1
            dircount = 0
            continue

# for i in range(0, n):
#     for j in range(0, m):
#         if(visit[i][j]==1):
#             count+=1

print(count)


