import sys
import heapq
n=int(sys.stdin.readline().rstrip())
arr=[]
for _ in range(n):
    x=int(sys.stdin.readline().rstrip())
    heapq.heappush(arr, x)

sum=0
while(len(arr)>=2):
    temp=0
    temp+=heapq.heappop(arr)
    temp+=heapq.heappop(arr)
    sum+=temp
    heapq.heappush(arr, temp)

print(sum)