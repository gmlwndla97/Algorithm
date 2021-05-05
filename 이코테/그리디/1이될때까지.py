import sys
n, k=map(int, sys.stdin.readline().rstrip().split())
cnt=0
# while(n!=1):
#     if(n%k==0):
#         n=n/k
#     else:
#         n=n-1
#     cnt+=1
#
# print(cnt)

while(True):
    target=(n//k)*k
    cnt+=(n-target)

    n=target
    if(n<k): break

    n=n/k
    cnt+=1

cnt+=(n-1)
print(int(cnt))

