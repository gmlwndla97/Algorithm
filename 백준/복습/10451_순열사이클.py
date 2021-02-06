import sys
t=int(sys.stdin.readline().rstrip())
ans=0

def dfs(start):
    if visit[start]==0:
        visit[start]=1
        dfs(arr[start])

for _ in range(0, t):
    n=int(sys.stdin.readline().rstrip())
    arr=list(map(int, sys.stdin.readline().rstrip().split()))
    visit=[0]*(n+1)
    arr.insert(0, 0)
    for i in range(1, n+1):
        if visit[i]==0:
            ans+=1
            dfs(i)

    print(ans)
    ans=0