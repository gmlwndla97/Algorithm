import sys

n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(0, n):
    str=sys.stdin.readline().rstrip()
    if str.startswith("push"):
        order, num=str.split(' ')
        arr.append(num)
    elif str.startswith("pop"):
        if len(arr)==0:
            print("-1")
        else:
            print(arr[len(arr)-1])
            arr.pop()
    elif str.startswith("size"):
        print(len(arr))
    elif str.startswith("empty"):
        if len(arr)==0:
            print(1)
        else:
            print(0)
    elif str.startswith("top"):
        if len(arr)==0:
            print(-1)
        else:
            print(arr[len(arr)-1])