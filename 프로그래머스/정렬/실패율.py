import sys
n=int(input())
stages=list(map(int, sys.stdin.readline().rstrip().split()))
result=[]
stages.sort()
for i in range(1, n+1):
    up=0
    down=0
    for j in stages:
        if(j>=i and j<=n+1):
            down+=1
        if(j==i):
            up+=1
    if(down==0):
        result.append((0, i))
    else:
        result.append((up/down, i))

result.sort(key=lambda x:-x[0])
for i in result:
    print(i[1])
