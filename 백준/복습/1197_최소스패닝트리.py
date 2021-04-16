import sys
v, e=map(int, sys.stdin.readline().rstrip().split())
parent=[0]*(v+1)
arr=[]
answer=0

for _ in range(e):
    a,b,c=map(int, sys.stdin.readline().rstrip().split())
    arr.append((a,b,c))
arr.sort(key=lambda x:(x[2], x[0], x[1]))

for i in range(1, v+1):
    parent[i]=i

def find_parent(x):
    if(parent[x]!=x): #다르면
        parent[x]=find_parent(parent[x])
    return parent[x]

def union(x, y):
    ##!!!!
    x=find_parent(x)
    y=find_parent(y)
    if(x<y):
        parent[y]=x
    else:
        parent[y]=x

for i in range(e):
    x, y, cost=arr[i]
    if(find_parent(x)!=find_parent(y)): #부모가 다른 경우
        union(x, y)
        answer+=cost
    else:
        continue


print(answer)