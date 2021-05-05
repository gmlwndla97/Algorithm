import sys
n=int(sys.stdin.readline().rstrip())
order=list(sys.stdin.readline().rstrip().split())
print(order)
arr=[[0]*n for _ in range(n)]
dir=['L','R','U','D']
dx=[0, 0, -1, 1]
dy=[-1,1,0,0]
x=0
y=0
for i in order:
    index=dir.index(i)
    nx=dx[index]+x
    ny=dy[index]+y
    if(nx>=0 and nx<n and ny>=0 and ny<n):
        x=nx
        y=ny
    else:
        continue

print(x+1, y+1, end=' ')