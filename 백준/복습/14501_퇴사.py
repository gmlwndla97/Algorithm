import sys
n=int(input())
ti=[0]
pi=[0]
dp=[0]*(n+1)
for i in range(0, n):
    t, p=map(int, sys.stdin.readline().rstrip().split())
    ti.append(t)
    pi.append(p)
maxval=0
for i in range(n, 0, -1):
    if(i+ti[i]<=(n+1)):
        if(i+ti[i]==(n+1)):
            dp[i]=max(maxval, dp[i]+pi[i])

        else:
            dp[i]=max(maxval, dp[i+ti[i]]+pi[i])
        if (maxval < dp[i]):
            maxval = dp[i]
    else:
        if(i+1<=n):
            dp[i]=dp[i+1] #무조건 새로 계산 안하는 거는 이전 꺼 그대로 가져오는거 필요함 !!!

print(max(dp))