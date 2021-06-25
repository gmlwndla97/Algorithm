import sys
n, m=map(int, sys.stdin.readline().rstrip().split())
answer=[]
def dfs(count):
    if(len(answer)==m):
        for i in range(0, m):
            print(answer[i], end=' ')
        print()
        return

    for i in range(0, n):
        answer.append(i+1)
        dfs(count+1)
        answer.pop()


dfs(0)