import sys
from collections import deque
q=deque()
n=int(sys.stdin.readline().rstrip())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
beforeidx=[]
idx=[]
ans=[]
def lower_bound(s, e, d):
    while(e-s>0):
        m=(s+e) //2
        if(ans[m] <d):
            s=m+1
        else:
            e=m

    return e
beforeidx=[0]*n
idx=[0]*n
beforeidx[0]=-1
ans.append(arr[0])
idx[0]=0

for i in range(1, n):
    if ans[len(ans)-1]<arr[i]: #벡터 맨 뒤보다 더 크면 push
        ans.append(arr[i])
        idx[len(ans)-1]=i
        beforeidx[i]=idx[len(ans)-2]
    else: #안크면 lowerbound로 찾은 곳에 삽입
        lower=lower_bound(0, len(ans), arr[i])
        ans[lower]=arr[i]
        idx[lower]=i
        if(lower==0):
            beforeidx[i]=-1
        else:
            beforeidx[i]=idx[lower-1]

print(len(ans))
index=idx[len(ans)-1]
result=[]

while(index!=-1):
    result.append(arr[index])
    index=beforeidx[index]

result.reverse()
for i in result:
    print(i, end=' ')

