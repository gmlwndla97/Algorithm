import sys
from collections import deque
q=deque()
fire=deque()
visit=[[0]*1000 for _ in range(1000)]
firevisit=[[0]*1000 for _ in range(1000)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
turn=0

def spreadFire(turn):
    while(fire):
        now_x=fire[0][0]
        now_y=fire[0][1]
        now_cnt=fire[0][2]
        if turn!=now_cnt:
            break
        fire.popleft()
        for i in range(0, 4):
            nx=dx[i]+now_x
            ny=dy[i]+now_y
            if (nx>=0 and nx<h and ny>=0 and ny<w):
                if arr[nx][ny]=='.' and firevisit[nx][ny]==0:
                    arr[nx][ny]='*'
                    firevisit[nx][ny]=1
                    fire.append((nx, ny, now_cnt+1))


def bfs(arr, turn):
    ##1. 일단 불을 먼저 퍼트림
    ##2. 그리고 상근이 동서남북 이동할 수 있으면 큐에 푸시. 이동한 곳은 빈 곳으로 바꿔주고
    ##3. 만약에 다음번에 맵 벗어나면 정답
    while(q):
        spreadFire(turn)
        now_x=q[0][0]
        now_y=q[0][1]
        now_cnt=q[0][2]
        arr[now_x][now_y]='@'

        if turn==now_cnt:
            q.popleft()
            arr[now_x][now_y]='.'

            for i in range(0, 4):
                nx=dx[i]+now_x
                ny=dy[i]+now_y
                if (nx>=0 and nx<h and ny>=0 and ny<w):
                    if visit[nx][ny]==0 and arr[nx][ny]=='.':
                        visit[nx][ny]=1
                        q.append((nx, ny, now_cnt+1))
                else:
                    if (arr[now_x][now_y]=='.'):
                        return now_cnt
        else:
            turn+=1

    return -1

t=int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    w, h= map(int, sys.stdin.readline().rstrip().split())
    arr=[list(map(str, sys.stdin.readline().rstrip())) for _ in range(h)]

    for i in range(0, h):
        for j in range(0, w):
            if arr[i][j]=='@':
                visit[i][j]=1
                q.append((i, j, 0))
            if arr[i][j]=='*':
                firevisit[i][j]=1
                fire.append((i, j, 0))

    ans=bfs(arr, turn)
    if ans!=-1:
        print(ans+1)
    else:
        print("IMPOSSIBLE")
    q = deque()
    fire = deque()
    visit = [[0] * 1000 for _ in range(1000)]
    firevisit = [[0] * 1000 for _ in range(1000)]