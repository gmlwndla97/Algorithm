import sys
x=int(input())
arr=[987654321]*(x+1)
arr[1]=0

for i in range(2, x+1):
    if(i%3==0):
        arr[i]=min(arr[i//3]+1, arr[i])
    if(i%2==0):
        arr[i]=min(arr[i//2]+1, arr[i])
    arr[i]=min(arr[i-1]+1, arr[i])

print(arr[x])