import sys
from itertools import combinations
n, m=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
comb=combinations(arr, 3)
comb=list(comb)
sum=0
diff=987654321
ans=0
for i in range(0, len(comb)):
    for j in range(0, 3):
        sum+=comb[i][j]
    if(sum<=m):
        if(abs(sum-m)<diff):
            diff=abs(sum-m)
            ans=sum
    sum=0

print(ans)