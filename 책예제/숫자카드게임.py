import sys
n, m=map(int, sys.stdin.readline().rstrip().split())
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
temp=[]
min=987654321
for i in range(0, n):
    min=arr[i][0]
    for j in range(0, m):
        if(arr[i][j]<min):
            min=arr[i][j]
    temp.append(min)

temp.sort()
print(temp[len(temp)-1])

