import sys
from collections import deque
q=deque()
n=int(sys.stdin.readline().rstrip())
graph=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dx=[-1, 0, 0, 1]
dy=[0,-1,1,0]
dist=[[0]*n for _ in range(n)]
visit=[[0]*n for _ in range(n)]
x=0
y=0
nowsize=2
eatsize=0
time=0

for i in range(0, n):
    for j in range(0, n):
        if(graph[i][j]==9):
            x, y=i, j
            graph[i][j]=0
            break

def bfs(x, y):
    #최단 거리 갱신
    dist = [[-1] * n for _ in range(n)]
    visit=[[0]*n for _ in range(n)]
    q.append((x, y))
    dist[x][y]=0
    visit[x][y]=1
    while(q):
        now_x, now_y=q[0]
        q.popleft()
        for i in range(0, 4):
            nx=dx[i]+now_x
            ny=dy[i]+now_y
            if(nx>=0 and nx<n and ny>=0 and ny<n):
                if(graph[nx][ny]<=nowsize and visit[nx][ny]==0):
                    #작거나 같은 곳만 지나갈 수 있음
                    dist[nx][ny]=dist[now_x][now_y]+1
                    visit[nx][ny]=1
                    q.append((nx, ny))
    return dist

def findfish(dist):
    fish_x=0
    fish_y=0
    min_dist=987654321
    for i in range(0 ,n):
        for j in range(0, n):
            if(dist[i][j]!=-1 and graph[i][j]>=1 and graph[i][j]<nowsize):
                #먹을 수 있음
                if(min_dist>dist[i][j]):
                    min_dist=dist[i][j]
                    fish_x, fish_y=i, j
    if(min_dist==987654321):
        return None
    else:
        return fish_x, fish_y, min_dist


while True:
    #bfs(x, y)
    #print(dist)
    value=findfish(bfs(x, y)) #이제 먹을 물고기 찾아야지
    if(value==None):
        print(time)
        break
    else:
        eatsize+=1
        if(eatsize>=nowsize):
            nowsize+=1
            eatsize=0
        #먹은 곳으로 위치 옮겨줌
        graph[value[0]][value[1]]=0
        x=value[0]
        y=value[1]
        time+=value[2]
