import sys
n=int(input())
arr=[]
for i in range(0, n):
    name, score=sys.stdin.readline().rstrip().split()
    score=int(score)
    arr.append((name, score))

arr=sorted(arr, key=lambda x:x[0])
for i in range(0, n):
    print(arr[i][0])