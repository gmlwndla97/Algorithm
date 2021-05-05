import sys
n,m = map(int, sys.stdin.readline().rstrip().split())
graph=[[987654321]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b=map(int, sys.stdin.readline().rstrip().split())
    graph[a][b]=1
    graph[b][a]=1

x, k=map(int, sys.stdin.readline().rstrip().split())

#자기 자신은 0으로 가는거 만들어줘야함!!!
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if(i==j):
            graph[i][j]=0

for mid in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j]=min(graph[i][j], graph[i][mid]+graph[mid][j])

#print(graph)
answer=graph[1][k]+graph[k][x]
if(answer>=987654321):
    print(-1)
else:
    print(answer)
