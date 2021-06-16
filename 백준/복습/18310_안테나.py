import sys
n=int(input())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

if(n%2!=0):
    mid=n//2
    print(arr[mid])
else:
    leftmid=(n//2)-1
    mid=n//2
    print(min(arr[leftmid], arr[mid]))