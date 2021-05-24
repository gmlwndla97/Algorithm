import sys
from collections import deque
n, k=map(int, sys.stdin.readline().rstrip().split())

arr=list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
s, x, y=map(int, sys.stdin.readline().rstrip().split())
number=[]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
for i in range(0, n):
    for j in range(0, n):
        number.append((arr[i][j], 0, i, j))
number.sort()
number=deque(number)

while number:
    virus=number[0][0]
    time=number[0][1]
    now_x=number[0][2]
    now_y=number[0][3]
    number.popleft()
    if(time==s):
      #  print(x-1, y-1)

        break

    for i in range(0, 4):
        nx=now_x+dx[i]
        ny=now_y+dy[i]
        if(nx>=0 and nx<n and ny>=0 and ny<n):
            if(arr[nx][ny]==0):
                #전염가능하면 전염.
                arr[nx][ny]=virus
                number.append((virus, time+1, nx, ny))

print(arr[x-1][y-1])