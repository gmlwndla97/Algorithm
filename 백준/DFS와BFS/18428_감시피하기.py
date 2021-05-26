import sys
import copy
from itertools import combinations
n=int(sys.stdin.readline().rstrip())
arr=[list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(n)]
temp=copy.deepcopy(arr)
can=[]
teacher=[]
student=[]
def check(temp):
    for i in teacher:
        tx=i[0]
        ty=i[1]
        while(ty>=0):
            if(temp[tx][ty]=='O'):
                break
            if(temp[tx][ty]=='S'):
                temp[tx][ty]='X'
            ty-=1

        tx = i[0]
        ty = i[1]
        while (tx >= 0):
            if (temp[tx][ty] == 'O'):
                break
            if (temp[tx][ty] == 'S'):
                temp[tx][ty] = 'X'
            tx -= 1

        tx = i[0]
        ty = i[1]
        while (tx<n):
            if (temp[tx][ty] == 'O'):
                break
            if (temp[tx][ty] == 'S'):
                temp[tx][ty] = 'X'
            tx +=1
        tx = i[0]
        ty = i[1]
        while (ty<n):
            if (temp[tx][ty] == 'O'):
                break
            if (temp[tx][ty] == 'S'):
                temp[tx][ty] = 'X'
            ty +=1



for i in range(0, n):
    for j in range(0, n):
        if(arr[i][j]=='X'):
            can.append((i, j))
        if(arr[i][j]=='T'):
            teacher.append((i, j))
        if(arr[i][j]=='S'):
            student.append((i,j))



comb=combinations(can, 3)
comb=list(comb)

for cc in comb:
    flag = False
    for i in range(0, 3):
        x=cc[i][0]
        y=cc[i][1]
        temp[x][y]='O'
    check(temp)
    temptemp=[]
    for i in range(0, n):
        for j in range(0, n):
            if(temp[i][j]=='S'):
                temptemp.append((i, j))
    temptemp.sort()
    student.sort()
    if(temptemp==student):
        flag=True
        break
    else:
        temp=copy.deepcopy(arr)


if(flag==True):
    print("YES")
else:
    print("NO")