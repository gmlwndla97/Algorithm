import sys
from collections import  deque

q=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
def bfs(x, y, cnt):
    q.append((x,y, cnt))
    while(q):
        front_x=q[0][0]
        front_y=q[0][1]
        front_cnt=q[0][2]
        q.popleft()
        #print(front_x, front_y)
        if front_x== n-1 and front_y==m-1:
            print(front_cnt)
            return
        visit[front_x][front_y]=1
        for i in range(0, 4):
            nx=dx[i]+front_x
            ny=dy[i]+front_y
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if arr[nx][ny]==1 and visit[nx][ny]==0:
                    visit[nx][ny]=1
                    q.append((nx, ny, front_cnt+1))




n, m=map(int, sys.stdin.readline().rstrip().split())
arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
#print(arr)
visit=[[0]*m for _ in range(n)]
#print(visit)

bfs(0,0, 1)