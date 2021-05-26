import sys
n=int(input())
number=list(map(int, sys.stdin.readline().rstrip().split()))
add, minus, mul, div= map(int, sys.stdin.readline().rstrip().split())
maxval=-1000000000
minval=1000000000
def dfs(index, sum):
    global add, minus, mul, div
    global minval, maxval
    if(index==n):
        minval=min(minval, sum)
        maxval=max(maxval, sum)

    else:
        if(add>0):
            add-=1
            dfs(index+1, sum+number[index])
            add+=1

        if(minus>0):
            minus-=1
            dfs(index+1, sum-number[index])
            minus+=1

        if(mul>0):
            mul-=1
            dfs(index+1, sum*number[index])
            mul+=1

        if(div>0):
            div-=1
            dfs(index+1, int(sum/number[index]))
            div+=1

dfs(1, number[0])
print(maxval)
print(minval)
