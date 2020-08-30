#####백준 시간초과 해결한 코드
import sys
from collections import  deque
q=deque()
cnt=0


arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]

# 정답을 찾을때까지
# 모든 경우의 수를 전진하면서, 스도쿠 유효성을 어기지 않는지 탐색
# 더이상 나아갈 길이 없으면
# 한칸 뒤로 후퇴

def backtrack(num):
    if num==cnt:
        for i in range(0, 9):
            for j in range(0,9):
                print(arr[i][j],end=' ')
            print()
        return True

    else:
        row,col=q[num]
        for i in range(1,10):
            arr[row][col]=i
            if(isValidSudoku(row,col)):
                b=backtrack(num+1)
                if(b): return b
        arr[row][col]=0
        return False


def isValidSudoku(row, col):
    ##시간 줄인 다른 검사 방식.

    for i in range(0, 9):
        if(arr[row][col]==arr[row][i] and i!=col):
            return False
        if(arr[row][col]==arr[i][col] and i!=row):
            return False

    for i in range(3*(row//3), 3*(row//3)+3):
        for j in range(3*(col//3), 3*(col//3)+3):
            if(arr[row][col]==arr[i][j]):
                if (row!=i and col!=j):
                    return False

    return True


for i in range(0, 9):
    for j in range(0, 9):
        if arr[i][j]==0:
            q.append((i,j));
            cnt+=1
num=0
backtrack(0)