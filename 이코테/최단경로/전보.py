import sys
import heapq

q=[]
n, m, c=map(int,sys.stdin.readline().rstrip().split())
distance=[987654321]*(n+1)
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x, y, z=map(int, sys.stdin.readline().rstrip().split())
    graph[x].append((y,z))

def dik(start):
    heapq.heappush(q, (0, c))
    distance[c]=0
    while q:
        nowdist, now=heapq.heappop(q)
        if distance[now]<nowdist:
            continue

        for i in graph[now]:
            newcost=i[1]+nowdist
            if(newcost<distance[i[0]]):
                distance[i[0]]=newcost
                heapq.heappush(q, (newcost,i[0]))
dik(c)

count=0 #전달할 수 있는 도시 개수
time=0 #최고 시간
for i in range(1, n+1):
    if distance[i]!=987654321 and i!=c:
        #길이 있으면
        count+=1
        if(distance[i]>time):
            time=distance[i]

print(count, time)
