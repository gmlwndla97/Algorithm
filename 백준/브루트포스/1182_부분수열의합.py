import sys
from itertools import combinations
n, s=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
cnt=0
for i in range(1, n+1):
    comb=combinations(arr, i)
    comb=list(comb)
    ans=0
    for k in range(0, len(comb)):
        for j in range(0, i):
            ans+=int(comb[k][j])
        #print(ans)
        if(ans==s):
            cnt+=1
        ans=0

print(cnt)