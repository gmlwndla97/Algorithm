import sys
str=sys.stdin.readline().rstrip()

ans=[]
for i in range(0, len(str)):
    ans.append(str[i:len(str)])

ans.sort()
for i in ans:
    print(i)