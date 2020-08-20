import sys
import math
arr=[]
n, m=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))

diff=987654321
sum=0
result=0
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum+=arr[i]
            sum+=arr[j]
            sum+=arr[k]
            if (m-sum)<diff and sum<=m:
                diff=m-sum
                result=sum
            sum=0

print(result)
