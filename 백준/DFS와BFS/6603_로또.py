import sys
def dfs(n, number, start, depth, visit):
    if (depth > 6):
        ans = []
        for i in range(0, n):
            if (visit[i] == 1):
                ans.append(number[i])
        for i in ans:
            print(i, end=' ')
        print()
        return

    for i in range(start, n):
        visit[i] = 1
        dfs(n, number, i + 1, depth + 1, visit)
        visit[i] = 0



while(True):
    answer=list(map(int, sys.stdin.readline().rstrip().split()))
    if(answer[0]==0):
        break
    n=answer[0]
    visit=[0]*n
    number=answer[1:]
    dfs(n, number, 0, 1, visit)
    print()

