import sys
n, m= map(int, sys.stdin.readline().rstrip().split())
r, c, dir=map(int, sys.stdin.readline().rstrip().split())
arr=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

turn_time=0
count=1
visit[r][c] = 1
while True:
    dir-=1
    if( dir==-1): dir=3
    nx=dx[dir]+r
    ny=dy[dir]+c
    if(arr[nx][ny]==0 and visit[nx][ny]==0):
        #청소하지 않은 공간 존재하면
        turn_time=0
        r=nx
        c=ny
        visit[r][c]=1
        count+=1
        continue #1번으로 돌아감
    else:
        turn_time+=1


    if(turn_time==4):
        nx=r-dx[dir]
        ny=c-dy[dir]
        if(arr[nx][ny]==1):
            break
        else:
            #한칸 후진 후 2번으로 돌아감
            r=nx
            c=ny
            turn_time=0
            continue


print(count)