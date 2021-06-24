import sys
n=int(input())
arr=list(map(int, sys.stdin.readline().rstrip().split()))

dp=[0]*n
dp[0]=arr[0]
dp[1]=max(dp[0], arr[1])
for i in range(2, n):
    dp[i]=max(dp[i-1], arr[i]+arr[i-2])

print(max(dp))