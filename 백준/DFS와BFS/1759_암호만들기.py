import sys
l, c=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(str, sys.stdin.readline().rstrip().split()))
arr.sort()
visit=[0]*c
mo=['a', 'e','i','o','u']
def check(visit, arr):
    mocount=0
    jacount=0
    flag=False
    for i in range(0, c):
        if(visit[i]==1):
            if(arr[i] in mo):
                mocount+=1
            else:
                jacount+=1
            if(mocount>=1 and jacount>=2):
                flag=True
                break

    if(flag==True):
        return True
    else:
        return False



def dfs(start, depth):
    global visit
    if(depth==l):
        if(check(visit, arr)==True):
            for i in range(0, c):
                if(visit[i]==1):
                    print(arr[i], end='')
            print()
            return

    for i in range(start, c):
        visit[i]=1
        dfs(i+1, depth+1)
        visit[i]=0


dfs(0, 0)