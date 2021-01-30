import sys
from itertools import combinations
import copy
##바이러스 0인 곳 중 순열로 3개 골라 모두 테스트
n, m=map(int, sys.stdin.readline().rstrip().split(' '))

visit=[[0]*(m) for _ in range(n)]
arr=[list(map(int, sys.stdin.readline().rstrip().split()))for _ in range(n)]
zero=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
temparr = copy.deepcopy(arr)  # 복사 배열

def dfs(x, y):
    visit[x][y]=1
    for i in range(0, 4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temparr[nx][ny]==0 and visit[nx][ny]==0:
                temparr[nx][ny]=2
                dfs(nx, ny)

for x in range(0, n):
    for y in range(0, m):
        if arr[x][y]==0:
            zero.append((x,y))


#이제 매번 3개씩 조합 골라서 벽세우고 카운트하고 ...
walls=combinations(zero,3)
walls=list(walls)
ans=0
for i in range(0, len(walls)):
    for j in range(0, 3):
        temparr[walls[i][j][0]][walls[i][j][1]]=1
    for k in range(0, n):
        for l in range(0, m):
            if temparr[k][l] == 2 and visit[k][l] == 0:
                dfs(k, l)

    # 다 끝난다음에는 다 초기화해주고 계산.
    cnt=0
    for k in range(0, n):
        for l in range(0, m):
            if temparr[k][l]==0:
                cnt+=1
    ans = max(ans, cnt)
    temparr = copy.deepcopy(arr)
    visit = [[0] * (m) for _ in range(n)]


print(ans)
