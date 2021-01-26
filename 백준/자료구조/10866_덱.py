import sys

n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(0, n):
    str=sys.stdin.readline().rstrip()
    if str.startswith("push_back"):
        order, num=str.split(' ')
        arr.append(int(num))
    elif str.startswith("push_front"):
        order, num=str.split(' ')
        arr.insert(0, int(num))
    elif str.startswith("pop_front"):
        if len(arr)==0:
            print(-1)
        else:
            print(arr.pop(0))
    elif str.startswith("pop_back"):
        if len(arr)==0:
            print(-1)
        else:
            print(arr.pop(len(arr)-1))
    elif str.startswith("size"):
        print(len(arr))
    elif str.startswith("empty"):
        if len(arr)==0:
            print(1)
        else: print(0)
    elif str.startswith("front"):
        if len(arr)==0: print(-1)
        else: print(arr[0])
    else:
        if len(arr)==0: print(-1)
        else: print(arr[len(arr)-1])