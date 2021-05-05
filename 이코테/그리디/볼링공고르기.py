import sys
n, m=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

count=0
for i in range(0, len(arr)):
    start=i
    for j in range(i+1, len(arr)):
        if(arr[start]!=arr[j]):
            count+=1

print(count)