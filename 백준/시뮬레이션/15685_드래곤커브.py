import sys
n=int(sys.stdin.readline().rstrip())
arr=[[0]*101 for _ in range(101)]
dx=[0, -1, 0, 1]
dy=[1, 0, -1, 0]
stack=[]
end_x=0
end_y=0
def make_dragon():
    tail=len(stack)
    for i in range(tail-1, -1, -1):
        newDir=(stack[i]+1)%4
        global end_x
        global end_y
        end_x=end_x+dx[newDir]
        end_y = end_y + dy[newDir]
        arr[end_x][end_y]=1
        stack.append(newDir)

for _ in range(0, n):
    y, x, d, g=map(int, sys.stdin.readline().rstrip().split())
    arr[x][y]=1
    end_x=x+dx[d]
    end_y=y+dy[d]
    arr[end_x][end_y]=1
    stack.append(d)
    for _ in range(0, g):
        make_dragon()
    cnt=0
    flag=False
    for i in range(0, 100):
        for j in range(0, 100):
            if(arr[i][j]==1 and arr[i+1][j]==1 and
            arr[i][j+1]==1 and arr[i+1][j+1]==1):
                #print(i, j)
                cnt+=1
    stack.clear()

print(cnt)