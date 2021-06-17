import sys
n=int(input())
tt=[]
pp=[]
dp=[0]*(n+1)
for _ in range(n):
    t, p=map(int,sys.stdin.readline().rstrip().split())
    tt.append(t)
    pp.append(p)

maxval=0
for i in range(n-1, -1, -1):
    if(i+tt[i]<=n):
        dp[i]=max(maxval, pp[i]+dp[i+tt[i]])
    else:
        dp[i]=dp[i+1]
    if(dp[i]>maxval):
        maxval=dp[i]

print(maxval)
