import sys
import copy
n, m=map(int, sys.stdin.readline().rstrip().split())
arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
ssum=[[0]*(m+1) for _ in range(n+1)]
ans=0
# def sum(x1, y1, x2, y2):
#     count=0
#     for i in range(x1, x2+1):
#         for j in range(y1, y2+1):
#             count+=arr[i][j]
#     return count

#값 미리 저장하는 경우
def sum(x1, y1, x2, y2):
    return ssum[x2+1][y2+1]-ssum[x2+1][y1]-ssum[x1][y2+1]+ssum[x1][y1]

for i in range(1, n+1):
    for j in range(1, m+1):
        ssum[i][j]=ssum[i-1][j]+ssum[i][j-1]-ssum[i-1][j-1]+arr[i-1][j-1]
# print(ssum)
#1번 사각형
for i in range(0, m-2):
    for j in range(i+1, m-1):
        r1=sum(0,0, n-1, i)
        r2=sum(0, i+1, n-1, j)
        r3=sum(0, j+1, n-1, m-1)

        temp=r1*r2*r3
        if temp>ans:
            ans=temp

#2번 사각형 (가로 3줄)
for i in range(0, n-2):
    for j in range(i+1, n-1):
        r1 = sum(0, 0, i, m-1)
        r2 = sum(i+1, 0, j, m-1)
        r3 = sum(j+1, 0, n-1, m-1)

        temp = r1 * r2 * r3
        if temp > ans:
            ans = temp

#3번 사각형
for i in range(0, m-1):
    for j in range(0,n-1):
        r1 = sum(0, 0, n-1, i)
        r2 = sum(0, i+1, j, m-1)
        r3 = sum(j+1, i+1, n-1, m-1)

        temp = r1 * r2 * r3
        if temp > ans:
            ans = temp

#4번 사각형
for i in range(0, m-1):
    for j in range(0, n-1):
        r1 = sum(0, 0,j,i)
        r2 = sum(j+1, 0, n-1, i)
        r3 = sum(0, i+1, n-1, m-1)

        temp = r1 * r2 * r3
        if temp > ans:
            ans = temp

    #5번 사각형
for i in range(0, n-1):
    for j in range(0, m-1):
        r1 = sum(0, 0, i, m-1)
        r2 = sum(i+1, 0, n-1, j)
        r3 = sum(i+1, j+1, n-1, m-1)

        temp = r1 * r2 * r3
        if temp > ans:
            ans = temp

            #6번 사각형
for i in range(0, m -1):
    for j in range(0, n-1):
        r1 = sum(0, 0, j, i)
        r2 = sum(0, i+1, j, m-1)
        r3 = sum(j+1, 0, n-1, m-1)

        temp = r1 * r2 * r3
        if temp > ans:
            ans = temp


print(ans)