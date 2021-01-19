import sys
n=int(sys.stdin.readline().rstrip())
list = []
for i in range(0, n):
    nn, name=sys.stdin.readline().rstrip().split(' ')
    list.append((int(nn), name))

list.sort(key=lambda x:x[0])
for i in range(0, n):
    print(list[i][0],list[i][1])
