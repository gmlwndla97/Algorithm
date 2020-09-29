import sys
sys.setrecursionlimit(2000)
def dfs(start):
    visit[start]=1
    next=int(numbers[start])
    if(visit[next]==0):
        dfs(next)
    return


t=int(sys.stdin.readline().rstrip())

for i in range(0, t):
    cnt = 0
    n = int(sys.stdin.readline().rstrip())
    visit=[0]*(n+1)
    numbers = list(map(int, input().split()))
    numbers=[0]+numbers ##맨앞에 0 추가 1부터 시작하도록..
    for j in range(1, n+1):
        if(visit[j]==0):
            dfs(j)
            cnt+=1
    print(cnt)

