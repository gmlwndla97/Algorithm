import sys

n, m=map(int, sys.stdin.readline().rstrip().split())
arr=[list( sys.stdin.readline().rstrip()) for _ in range(n)]

white=[[0]*8 for _ in range(8)]
black=[[0]*8 for _ in range(8)]


for i in range(0, 8):
    for j in range(0,8):
            if i%2==0:
                if j%2==0:
                    white[i][j]='W'
                else:
                    white[i][j]='B'
            else:
                if j % 2 == 0:
                    white[i][j] = 'B'
                else:
                    white[i][j] = 'W'

for i in range(0, 8):
    for j in range(0,8):
            if i%2==0:
                if j%2==0:
                    black[i][j]='B'
                else:
                    black[i][j]='W'
            else:
                if j % 2 == 0:
                    black[i][j] = 'W'
                else:
                    black[i][j] = 'B'

#먼저 white 확인
min=987654321
cnt=0
for i in range(0, n):
    for j in range(0,m):
        if i+8<=n and j+8<=m:
            for k in range(0, 8):
                for l in range(0, 8):
                    if arr[i+k][j+l]!=white[k][l]:
                        cnt+=1

            if cnt<min:
                min=cnt
            cnt=0

cnt=0
for i in range(0, n):
    for j in range(0,m):
        if i+8<=n and j+8<=m:
            for k in range(0, 8):
                for l in range(0, 8):
                    if arr[i+k][j+l]!=black[k][l]:
                        cnt+=1
            if cnt<min:
                min=cnt
            cnt=0

print(min)