import sys
from itertools import permutations
sys.setrecursionlimit(100000)
n=int(sys.stdin.readline().rstrip())
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# order=[]
# for i in range(0, n):
#     order.append(i)
order=[i for i in range(n)]

ans=987654321
permuOrder=permutations(order, n)
# permuOrder=list(permuOrder)
def route(list):
    temp=0
    global flag
    for i in range(0, len(list)-1):
        if(arr[list[i]][list[i+1]]==0):
            return -1
        temp+=arr[list[i]][list[i+1]]

    if arr[list[len(list)-1]][list[0]]==0:
        return -1
    else:
        temp+=arr[list[len(list)-1]][list[0]]
    return temp

for i in permuOrder:
    result=route(i)
    if result!=-1:
        if result<ans:
            ans=result
print(ans)