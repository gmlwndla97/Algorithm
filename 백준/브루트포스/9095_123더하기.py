import sys
t=int(sys.stdin.readline().rstrip())
arr=[0]*12
arr[0]=1
arr[1]=1
arr[2]=2
for _ in range(0, t):
    n=int(sys.stdin.readline().rstrip())
    for i in range(3, n+1):
        arr[i]=arr[i-3]+arr[i-2]+arr[i-1]

    print(arr[n])
