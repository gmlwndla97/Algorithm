from collections import deque
import sys

q=deque()
k=int(input())
sum=0
num=[]
for _ in range(k):
    num.append(int(sys.stdin.readline().strip()))
for i in num:
    if i==0:
        q.pop()
        continue
    else:
        q.append(i)

while q:
   front=q[0]
   sum=sum+front
   q.popleft()

print(sum)