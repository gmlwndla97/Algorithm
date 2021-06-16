import sys
n=int(input())
tt=[]
pp=[]
for _ in range(n):
    t, p=map(int,sys.stdin.readline().rstrip().split())
    tt.append(t)
    pp.append(p)

maxval=0
dp=[0]*n
for i in range(n-1, -1, -1):
    if(i+tt[i]>=n):
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1], dp[i+tt[i]]+p[i])

print(max(dp))