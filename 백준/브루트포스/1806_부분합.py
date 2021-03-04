import sys
n, s=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
low=0
high=0
minlen=987654321
sum=0
flag=False


sum=arr[0]
while(True):
    if(sum>=s):
        if(abs(high-low)+1 <minlen):
            minlen=abs(high-low)+1

        if (low == n-1): break
        sum -= arr[low]
        low += 1

    else:
        if(high == n-1): break
        if(high<n-1):
            high+=1
            sum+=arr[high]

if(minlen==987654321):
    print(0)
else:
    print(minlen)