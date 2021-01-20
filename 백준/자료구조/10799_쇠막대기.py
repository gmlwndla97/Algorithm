import sys

str=sys.stdin.readline().rstrip()
prev=''
now=''
arr=[]
ans=0
for i in str:
    if i=='(':
        #새로 열리는 괄호
        arr.append(i)
    elif i==')' and prev=='(':
        #레이저
        arr.pop()
        ans+=len(arr)
    elif i==')' and prev==')':
        arr.pop()
        ans+=1
    prev=i

print(ans)