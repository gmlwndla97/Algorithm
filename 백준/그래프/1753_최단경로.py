import sys
import heapq
pq=[]

v, e=map(int, sys.stdin.readline().rstrip().split())
k=int(sys.stdin.readline().rstrip())
arr=[[] for _ in range(v+1)]


dist=[987654321]*(v+1)
dist[k]=0
for i in range(0, e):
    a, b, c=map(int, sys.stdin.readline().rstrip().split())
    arr[a].append((b, c))

heapq.heappush(pq, (0, k))
while pq:
    nowdist, nownode=heapq.heappop(pq)
    if dist[nownode]<nowdist:
        continue
    for i in arr[nownode]:
        sidecost=i[1]
        sidenode=i[0]
        if(dist[sidenode]>nowdist+sidecost):
            dist[sidenode]=nowdist+sidecost
            newcost=nowdist+sidecost
            heapq.heappush(pq, (newcost, sidenode))


for i in range(1, v+1):
    if dist[i]==987654321:
        print("INF")
    else:
        print(dist[i])
