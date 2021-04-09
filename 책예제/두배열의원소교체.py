import sys
n, k=map(int, sys.stdin.readline().rstrip().split())
a=list(map(int ,sys.stdin.readline().rstrip().split()))
b=list(map(int ,sys.stdin.readline().rstrip().split()))
a.sort()
b=sorted(b, reverse=True)
for i in range(0, k):
    if(a[i]<b[i]):
        a[i], b[i]=b[i], a[i]
    else: #그렇게 정렬했는데 지금 가지고 있는게 더 크면
        #바꿀필요없으니까 그냥 탈출해도 됨
        break
answer=0
for i in a:
    answer+=i
print(answer)