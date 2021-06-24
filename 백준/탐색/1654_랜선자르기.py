import sys
k, n=map(int, sys.stdin.readline().rstrip().split())
arr=[]
for _ in range(k):
    num=int(sys.stdin.readline().rstrip())
    arr.append(num)

start=1
end=max(arr)

while(start<=end):
    mid=(start+end)//2

    num=0
    for i in arr:
        num+=i//mid
    if(num>=n):
        start=mid+1
    else:
        end=mid-1

print(end)
