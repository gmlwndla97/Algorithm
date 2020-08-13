import sys

a,b=(sys.stdin.readline().rstrip().split())
reva=a[::-1]
revb=b[::-1]
if int(reva)>int(revb):
    print(reva)
else:
    print(revb)