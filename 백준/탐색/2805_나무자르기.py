import sys
n, m=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
start=0
end=max(arr)


answer=0
while(start<=end):
    mid=(start+end)//2
    diff=0
    for i in arr:
        if(i>mid):
            diff+=(i-mid)
    if(diff==m):
        answer=max(answer, mid)
        break
    elif(diff<m):
        end=mid-1
    else:
        #일단 여기는 그 최소 길이는 충족했는데 답이 아닐 수 있는거니까
        #기록을 해놓는거지 ...
        answer=max(answer, mid)
        start=mid+1

print(answer)

