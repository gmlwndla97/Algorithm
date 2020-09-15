#arr로 구현해보기.
import sys

n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(0, n):
    order=sys.stdin.readline().rstrip()

    if order.startswith('push'):
        #X는 order[5:]번째에 있긴한데... 다른 방법이 있을 것 같음
        num=int(order[5:])
        arr.append(num)

    elif order.startswith('pop'):
        if(len(arr))>0:
            print(arr[len(arr)-1])
            del arr[len(arr)-1]
        else:
            print(-1)

    elif order.startswith('size'):
        print(len(arr))

    elif order.startswith('empty'):
        if len(arr)==0:
            print(1)
        else:
            print(0)

    elif order.startswith('top'):
        if len(arr)>0:
            print(arr[len(arr)-1])
        else:
            print(-1)