import sys
import heapq
from queue import PriorityQueue

h=[]
que = PriorityQueue()
n=int(sys.stdin.readline().rstrip())
for i in range(0, n):
    x=int(sys.stdin.readline().rstrip())
    if x!=0:
        heapq.heappush(h, x)
    else:
        if len(h)==0:
            print(0)
        else:
            print(heapq.heappop(h))