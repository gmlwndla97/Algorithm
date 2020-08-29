#####백준 시간초과 해결못함
# ### 코드만 맞음
#
#
import sys
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
# 정답을 찾을때까지
# 모든 경우의 수를 전진하면서, 스도쿠 유효성을 어기지 않는지 탐색
# 더이상 나아갈 길이 없으면
# 한칸 뒤로 후퇴

def backtrack(index):
    #index=81까지 도달한거면 마지막까지 잘 도착한것이므로 true
    if index==81:
        for i in range(0,9):
            for j in range(0, 9):
                print(arr[i][j], end=' ')
            print()
        return True
    row=index//9
    col=index%9
    now=arr[row][col]

    if(now!=0): #숫자가 있다면 다음칸으로
        return backtrack(index+1)
    else:
        for i in range(1, 10): #1~9까지 숫자 돌아가면서 채움
            arr[row][col]=i
            if isValidSudoku()==True:
                isRight=backtrack(index+1) #여기서 정답이라면 정답 리턴
                if isRight==True:
                    return isRight

        arr[row][col]=0
        return False




def isValidSudoku():
    visit=[0]*10
    #가로, 세로, 3x3칸검증 세가지를 하겠다
    for i in range(0, 4):
        #한줄의 규칙
        for j in range(0,9):
            visit = [0] * 10
            for k in range(0,9):
                cur=0
                if (i==0): #가로줄 검증
                    cur=int(arr[j][k])
                elif(i==1): #세로줄 검증
                    cur = int(arr[k][j])
                else: #섭그리드 검증
                    #j는 몇번째 섭그리드인지
                    #k는 그 안에서 몇번쨰 칸인지
                    cur=arr[j//3*3+k//3][j%3*3+k%3]
                if cur == 0: continue
                val = int(cur)
                if (visit[val - 1] == 1): return False
                visit[val - 1] = 1

    return True





def solveSudoku():
    backtrack(0)

solveSudoku()