import sys

n=int(sys.stdin.readline().rstrip())
left=0
right=0
flag=False

for i in range(0, n):
    str=sys.stdin.readline().rstrip()
    left = 0
    right = 0
    flag=False
    if str.startswith(')'):
        flag=True
    else:
        for j in str:
            if j=='(':
                left+=1
            elif j==')':
                right+=1
            if(right>left):
                flag = True

    if flag==True or right!=left:
        print("NO")
    else:
        print("YES")
