import sys
n=int(sys.stdin.readline().rstrip())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
start=0
end=n-1
mid=(start+end)//2
print(arr[mid])