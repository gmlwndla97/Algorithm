import sys
n, k=map(int, sys.stdin.readline().rstrip().split(' '))
arr=[]
arr=list(map(int, sys.stdin.readline().rstrip().split(' ')))
#print(arr)
arr.sort()
print(arr[k-1])