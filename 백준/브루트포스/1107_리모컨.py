import sys
from collections import deque
q=deque()
n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())
available=[1]*10
if(m!=0):
    mal=list(map(int, sys.stdin.readline().rstrip().split()))
else:
    mal=[]
#1. +, -버튼으로 움직이기

minval=abs(n-100)

#2. 0~1000000 까지 돌면서 다 해보기
for i in range(0, 1000001):
    st=str(i)
    flag=False
    for j in range(0, len(st)):
        if int(st[j]) in mal:
            flag=True
            break

    if flag==False : #버튼이 고장난 경우엔
        minval=min(minval, abs(i-n)+ len(str(i)))

    flag=False

print(minval)