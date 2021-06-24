import sys
t=int(input())
for _ in range(t):
    n, m=map(int, sys.stdin.readline().rstrip().split())
    array=list(map(int, sys.stdin.readline().rstrip().split()))
    arr=[]
    dp=[[0]*m for _ in range(n)]
    index=0
    for i in range(0, n):
        arr.append(array[index:index+m])
        index+=m
    for i in range(0, n):
        dp[i][0]=arr[i][0]


    for j in range(1, m):
        for i in range(0, n):
            if(i==0):
                dp[i][j]=arr[i][j]+max(dp[i][j-1], dp[i+1][j-1])
            elif(i==n-1):
                dp[i][j]=arr[i][j]+max(dp[i-1][j-1], dp[i][j-1])
            else:
                dp[i][j]=arr[i][j]+max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

    maxval=0
    for i in range(0, n):
        maxval=max(maxval, dp[i][m-1])

    print(maxval)