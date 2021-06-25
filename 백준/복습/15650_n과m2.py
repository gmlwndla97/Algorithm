import sys
n, m=map(int, sys.stdin.readline().rstrip().split())
visit=[0]*(n)
answer=[]
def dfs(start, count):
    if(count==m):
        for j in range(0, n):
            if(visit[j]==1):
                print(j+1, end=' ')
        print()

    for i in range(start, n):
        visit[i] = 1
        dfs(i + 1, count + 1)
        visit[i] = 0


# number=[]
# for i in range(1, n+1):
#     number.append(i)

dfs(0, 0)
