import sys
from string import ascii_lowercase
str=sys.stdin.readline().rstrip()
alpha=list(ascii_lowercase)
visit=[-1]*26
for i in range(0, len(str)):
    #print(ord(str[i])-97)
    if visit[ord(str[i])-97]==-1:
        visit[ord(str[i])-97]=i

for i in visit:
    print(i, end=' ')