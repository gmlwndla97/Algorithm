import sys

a, b, c, d=map(str, sys.stdin.readline().rstrip().split())
ab=a+b
cd=c+d

print(int(ab)+int(cd))