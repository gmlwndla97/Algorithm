import sys
v, e=map(int, sys.stdin.readline().rstrip().split(' '))
edge=[]
ans=0

def find(a):
    if a==parent[a]:
        return a
    else:
        b=find(parent[a])
        parent[a]=b
        return b

def merge(a, b):
    aParent=find(a)
    bParent=find(b)
    parent[bParent]=aParent

for i in range(0, e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))
    edge.append((c, a, b))

parent=[0]*(v+1)
for i in range(1, v+1):
    parent[i]=i

edge.sort(key=lambda x:x[0])
#print(edge)

for i in range(0, e):
    if(find(edge[i][1]) != find(edge[i][2])): #부모가 다르면
        #추가
        merge(edge[i][1], edge[i][2])
        ans+=edge[i][0]

print(ans)