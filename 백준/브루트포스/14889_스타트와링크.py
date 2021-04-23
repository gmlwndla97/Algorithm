import sys
from itertools import combinations

n=int(sys.stdin.readline().rstrip())
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
num=[]
for i in range(0, n):
    num.append(i)

visit=[0]*(n)
comb=combinations(num, n//2)
comb=list(comb)

minanswer=987654321
for i in comb:
    visit = [0] * (n)
    for j in range(0, n//2):
        visit[i[j]]=1
    start=[]
    link=[]
    for j in range(0, len(visit)):
        if visit[j]==1:
            start.append(j)
        else:
            link.append(j)

    startcomb=combinations(start, 2)
    linkcomb=combinations(link, 2)
    startcomb=list(startcomb)
    linkcomb=list(linkcomb)

    start_sum=0
    link_sum=0
    for j in startcomb:
        x_index=j[0]
        y_index=j[1]
        start_sum+=arr[x_index][y_index]
        start_sum+=arr[y_index][x_index]
    for j in linkcomb:
        x_index = j[0]
        y_index = j[1]
        link_sum += arr[x_index][y_index]
        link_sum += arr[y_index][x_index]

    minanswer=min(minanswer, abs(start_sum-link_sum))

print(minanswer)