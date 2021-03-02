import sys
n, m=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
count=0
low=0
high=0
while(True):
    temp=arr[low:high+1]
   # print(temp)
    sum=0
    for i in temp:
        sum=sum+i

    if(sum<m): high+=1
    elif(sum>=m):
        if(sum==m):
            count+=1
        low+=1
    if(high==n):
        break


print(count)