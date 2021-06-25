import sys
from collections import deque
import heapq
n=int(input())
m=int(input())
arr=[[] for _ in range(n+1)]
dist=[987654321]*(n+1)
q=[]
for _ in range(m):
    x, y, w=map(int, sys.stdin.readline().rstrip().split())
    arr[x].append((y, w))
 #   arr[y].append((x, w))


start, end=map(int, sys.stdin.readline().rstrip().split())
dist[start]=0
heapq.heappush(q, (0, start))
while(q):
    tonowdist=q[0][0]
    nownode=q[0][1]
    heapq.heappop(q)

    if(dist[nownode]<tonowdist):
        #지금 nownode인데, 지금까지 온 길이인 tonowdist보다이미 작다면 갱신할 필요없다는 뜻
        continue

    for i in arr[nownode]:
        nextnode=i[0]
        addcost=i[1]

        if(dist[nextnode]>tonowdist+addcost):
            dist[nextnode]=tonowdist+addcost
            heapq.heappush(q, (dist[nextnode], nextnode))


print(dist[end])