import sys
ans=sys.stdin.readline().rstrip()
start=0
## 0~9, 10~19, 20~29 ...
value=len(ans)//10
while value>0:
    print(ans[start:start+10])
    start+=10
    value-=1

print(ans[start:len(ans)])