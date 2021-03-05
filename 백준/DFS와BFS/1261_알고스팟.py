import sys
import heapq
dx=[-1,1,0,0]
dy=[0,0,-1,1]
m, n=map(int, sys.stdin.readline().rstrip().split())
arr=list(list(map(int, sys.stdin.readline().rstrip()))
         for _ in range(n))
wall=[[987654321]*m for _ in range(n)]
q=[]
#pq.put(n), pq.put((우선순위,값)), pq.get(n) : 삭제
heapq.heappush(q, [0, 0, 0])
wall[0][0]=0
while(q):
    nowP, now_x, now_y=heapq.heappop(q)
    if (now_x==n-1 and now_y==m-1):
        print(nowP)
        break
    for i in range(0, 4):
        nx=dx[i]+now_x
        ny=dy[i]+now_y
        if(nx>=0 and nx<n and ny>=0 and ny<m):
            nw=nowP+arr[nx][ny]
            if(nw<wall[nx][ny]):
                wall[nx][ny]=nw
                heapq.heappush(q, [nw, nx, ny])

