import sys
from itertools import permutations
n=int(sys.stdin.readline().rstrip())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
ans=0
perm=permutations(arr, n)
perm=list(perm)
for i in range(0, len(perm)):
    temp=0
    for j in range(0, n-1):
        temp+=abs(perm[i][j]-perm[i][j+1])
        if temp>ans:
            ans=temp
            temp=0

print(ans)
