import sys
n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(0, n):
    x, y= map(int, sys.stdin.readline().rstrip().split())
    arr.append((x,y))

sortedarr=[]
sortedarr=sorted(arr, key=lambda  x:(x[0], x[1]))

for i in range(0, n):
    print(sortedarr[i][0], sortedarr[i][1])