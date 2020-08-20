import sys
from collections import deque
q=deque()
ranking=deque() #결과 순위 저장할 큐
n=int(sys.stdin.readline().rstrip())
for i in range(0, n):
    x, y=map(int, sys.stdin.readline().rstrip().split())
    q.append((x,y))

turn=0
for i in range(0, n):
    rank=0
    for k in range(0, n):
        myw, myh=q[turn]
        if k!=turn:
           w, h=q[k]
           if w>myw and h>myh:
               rank+=1
    turn+=1
    ranking.append(rank + 1)

for i in ranking:
    print(i, end=' ')
