import sys
n=int(sys.stdin.readline().rstrip())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline().rstrip())
find=list(map(int, sys.stdin.readline().rstrip().split()))
count=[0]*1000001

for i in range(0, len(arr)):
    count[arr[i]]+=1

sortedArr=[]
for i in range(0, 1000001):
    for j in range(count[i]):
        sortedArr.append(i)

for i in find:
    if i in sortedArr:
        print("Yes")
    else:
        print("no")