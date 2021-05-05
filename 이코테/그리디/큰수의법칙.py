import sys
n, m, k=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

ans=0

loop=0
while(True):
    if(loop+k>m):
        diff=m-loop
        for i in range(0, diff):
            ans += arr[n - 1]
        break

    for i in range(0, k):
        ans+=arr[n-1]
    loop+=k
    if(loop<m):
        ans+=arr[n-2]
        loop+=1

"""
loop=m
while(True):
    for i in range(0, k):
        if(loop==0):
            break
        ans+=arr[n-1]
        loop-=1
    if(loop==0): break
    ans+=arr[n-2]
    loop-=1
    """
print(ans)


