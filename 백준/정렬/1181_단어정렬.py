import sys
n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(0, n):
    str=sys.stdin.readline().rstrip()
    arr.append((len(str),str))

arr=set(arr)
arr=list(arr)
arr.sort(key=lambda x:(x[0], x[1]))
for i in arr:
    print(i[1])


