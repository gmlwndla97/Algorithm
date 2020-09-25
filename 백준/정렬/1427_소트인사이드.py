import sys
from queue import PriorityQueue
q=PriorityQueue()
n=sys.stdin.readline().rstrip()
for i in range(0, len(n)):
    q.put((int(n[i])*(-1),int(n[i])))

while q.qsize():
    print(q.get()[1],end='')

