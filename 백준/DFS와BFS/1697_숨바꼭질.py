import sys
from collections import deque
n, k=map(int, sys.stdin.readline().rstrip().split(' '))

visit=[0]*200001
q=deque()
q.append((n, 0))
visit[n]=1

while q:
    now, count=q[0]
    q.popleft()
    if now==k:
        print(count)
        break
    if(visit[now-1]==0 and now-1>=0 and now-1<=100000 ):
        visit[now-1]=1
        q.append((now-1, count+1))
    if(visit[now+1]==0 and now+1>=0 and now+1<=100000):
        visit[now+1]=1
        q.append((now+1, count+1))
    if(visit[now*2]==0 and now*2>=0 and now*2<=100000):
        visit[now*2]=1
        q.append((now*2, count+1))




