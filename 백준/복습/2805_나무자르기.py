import sys
n, m=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

start=0
end=arr[n-1]
answer=0
while(start<=end):
    mid=(start+end)//2

    sum=0
    for i in arr:
        if(i>mid):
            sum+=(i-mid)

    if(sum>=m):
        start=mid+1
    else:
        end=mid-1


print(end)
