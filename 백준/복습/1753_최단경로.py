import sys
import heapq
vertex, e= map(int, sys.stdin.readline().rstrip().split())
start=int(input())
dist=[987654321]*(vertex+1)
dist[start]=0
graph=[[]*(vertex+1) for _ in range(vertex+1)]
for _ in range(0, e):
    u,v,w=map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((v, w))

q=[]
heapq.heappush(q, (0, start))

while q:
    nowdist=q[0][0] #지금 여기까지오는데 최단거리
    nownode=q[0][1] #지금 온 여기
    heapq.heappop(q)
    if(dist[nownode]<nowdist):
        continue

    #지금 도착한 여기랑 인접한애들 다 검사.
    for i in graph[nownode]:
        sidenode=i[0]
        sidedist=i[1]
        if(dist[nownode]+sidedist<dist[sidenode]):
            dist[sidenode]=dist[nownode]+sidedist
            heapq.heappush(q, (dist[sidenode], sidenode))
#print(dist)
for i in range(1, vertex+1):
    if(dist[i]==987654321):
        print("INF")
    else:
        print(dist[i])
