import sys
alpha=[0]*26
str=sys.stdin.readline().rstrip()
for i in str:
    alpha[ord(i)-97]+=1
for i in alpha:
    print(i,end=' ')