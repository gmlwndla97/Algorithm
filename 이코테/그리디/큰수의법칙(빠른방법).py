import sys
n, m, k=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
ans=0
count=(m//(k+1))*k + (m%(k+1))
ans+=count*arr[n-1]
ans+=(m//(k+1))*arr[n-2]

print(ans)