import sys
n, m= map(int, sys.stdin.readline().rstrip().split())
arr=[]
ans=[]
parent=[0]*(n+1)
for i in range(1, n+1):
    parent[i]=i
def find(x):
    if(x==parent[x]):
        #자기 자신을 가르키고 있으면
        return x
    else:
        #위에 더 찾아서 root찾아야 한다면 재귀.
        pp=find(parent[x])
        parent[x]=pp
        return pp

def merge(x, y):
    px=find(x)
    py=find(y)
    parent[py]=px

for _ in range(m):
    x, y, w=map(int, sys.stdin.readline().rstrip().split())
    arr.append((w, x, y))
arr.sort()

#크루스칼
for i in range(m):
    if(find(arr[i][1])!=find(arr[i][2])):# 부모가 다르면 합치기
        merge(arr[i][1], arr[i][2])
        ans.append(arr[i][0])

ans.sort()
answer=0
for i in range(0, len(ans)-1):
    answer+=ans[i]


print(answer)

