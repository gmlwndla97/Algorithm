import sys
import itertools
##바이러스 0인 곳 중 순열로 3개 골라 모두 테스트
n, m=map(int, sys.stdin.readline().rstrip().split(' '))

arr=[[0]*(n) for _ in range(m)]
visit=[[0]*(n) for _ in range(m)]
zero=[]
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
for i in range(0, n):
    for j in range(0, m):
        if(arr[i][j]=='0'):
            zero.append((i,j))


wall=itertools.combinations(zero, 3)
print(list(wall))

