######파이썬으로 풀면 백준 시간 통과는 못한다..
######방식만 맞게 짠 코드

import sys
n=int(sys.stdin.readline().rstrip())
cnt=[]
num=0
def promising (row, col):
    for i in range(0, row):
        if arr[i][col]==1:
            return False

    #여기까지 왔으면 row 검사는 끝난것이므로 이제 대각선 검사
    ##1. 왼쪽 위 방향 대각선 검사
    x=row-1
    y=col-1
    while x>=0 and y>=0:
        if arr[x][y]==1:
            return False
        else:
            x-=1
            y-=1

    ##2. 오른쪽 위  방향 대각선 검사
    x=row-1
    y=col+1
    while x>=0 and y<n:
        if arr[x][y]==1:
            return False
        else:
            x-=1
            y+=1

    return True

def queen(row):
    # 맨마지막줄 도착할때까지
    #모든 경우의 수를 전진하면서, 퀸을 놓을 수 있는지 확인하면서 탐색
    # 놓을 수 없다면 한줄 위로 후퇴
    if row==n:
        cnt.append(1)
        return

    else:
        for col in range(0, n): #이제 열검사
            if arr[row][col]==0:
                if promising(row, col)==True:
                    arr[row][col]=1
                    queen(row+1)
                    arr[row][col]=0

    return

arr=[[0]*n for _ in range(n)]
queen(0)
print(len(cnt))