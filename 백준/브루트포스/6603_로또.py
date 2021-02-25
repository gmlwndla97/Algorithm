import sys
from itertools import combinations
ans=''
while(True):
    arr=list(map(int, sys.stdin.readline().rstrip().split()))
    if(arr[0]==0):
        break
    else:
        comb=combinations(arr[1:], 6)
        comb=list(comb)
        for i in range(0, len(comb)):
            for j in range(0, 6):
                print(comb[i][j], end=' ')
            print()
        print()