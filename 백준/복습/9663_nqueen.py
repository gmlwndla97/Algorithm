import sys
n=int(sys.stdin.readline().rstrip())

arr=[[0]*n for _ in range(n)]
answer=0
def promising(row, col):
    global arr
    #유망성 검사.
    #1. 내 위로 같은 row 겹치는지 확인..
    for i in range(0, row):
        if(arr[i][col]==1):
            return False

    #2. 내 대각선 겹치는지 확인
    #2-1. 오른쪽 아래로.
    x=row
    y=col
    while(x>=0 and y>=0):
        if(arr[x][y]==1):
            return False
        x-=1
        y-=1

    x=row
    y=col
    while(x>=0 and y<n):
        if(arr[x][y]==1):
            return False
        x-=1
        y+=1
    return True

def dfs(row):
    if(row==n):
        global answer
        answer+=1

    for i in range(0, n):
        if(promising(row, i)==True):
            arr[row][i]=1
            dfs(row+1 )
            arr[row][i]=0

dfs(0)
print(answer)