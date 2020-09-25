import sys
#############백준 시간초과 해결안됨
from queue import PriorityQueue
q=PriorityQueue()

n=int(sys.stdin.readline().rstrip())
for i in range(0, n):
    q.put(int(sys.stdin.readline().rstrip()))

while q.qsize():
    print(q.get())