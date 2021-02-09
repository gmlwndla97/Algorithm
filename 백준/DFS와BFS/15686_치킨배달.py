import sys
from collections import deque
from itertools import combinations
import copy

chicken=deque()
house=deque()

n, m=map(int, sys.stdin.readline().rstrip().split())
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
min_city=987654321 #모든 집마다의 치킨거리
minval=987654321
ans=0

def remove(left):
    global m

    #이제 다 바꿨으니까 최소 치킨거리 구하기.
    for i in range(0, len(house)):
        x=house[i][0]
        y=house[i][1]
        for j in range(0, m):
            chi_x=left[j][0]
            chi_y=left[j][1]
            global min_city
            min_city=min(min_city, (abs(x-chi_x)+abs(y-chi_y)))
        global ans
        ans+=min_city
        min_city=987654321


for i in range(0, n):
    for j in range(0, n):
        if arr[i][j]==2:
            chicken.append((i, j))
        if arr[i][j]==1:
            house.append((i,j))

left=combinations(chicken, m)
left=list(left)
for i in range(0, len(left)):
    remove(left[i])
    minval=min(minval, ans)
    ans=0


print(minval)