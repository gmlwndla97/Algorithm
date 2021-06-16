import sys
n=int(input())
arr=[[] for _ in range(n)]
for i in range(n):
    come=list(map(int,input().split()))
    arr[i]=come


dp=[[-1]*n for _ in range(n)]
dp[0][0]=arr[0][0]


for i in range(1, n): #3일때
    for j in range(0, i+1): #1, 2, 3
        if(j==0):
            dp[i][j]=arr[i][j]+dp[i-1][j]
        else:
            dp[i][j]=arr[i][j]+max(dp[i-1][j], dp[i-1][j-1])

print(max(map(max, dp)))