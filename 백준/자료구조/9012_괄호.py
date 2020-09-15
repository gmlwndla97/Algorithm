import sys

#일단은 왼쪽 괄호 들어온 개수에 맞춰 오른쪽 괄호가 들어와야되는 것임.
#왼쪽 괄호 들어온 개수보다 오른쪽이 많으면 그순간 탈락
#작으면 쌍 맞춰 지워가면서 마지막에 짝이 맞는지 확인

t=int(sys.stdin.readline().rstrip())

for i in range(0, t):
    str=sys.stdin.readline().rstrip()
    leftcount = 0
    rightcount = 0
    total = 0
    flag=False
    for j in range(0, len(str)):
        if str[j]=='(':
            leftcount+=1
            total+=1
        elif str[j]==')':
            rightcount+=1
            total=total-1
            if rightcount>leftcount:
                flag=True
                break

    if total==0:
        print('YES')
    elif total!=0 or flag==True:
        print('NO')
