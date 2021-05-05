import sys
ans=sys.stdin.readline().rstrip()
mid=len(ans)//2
left=0
right=0
for i in range(0, mid):
    left+=int(ans[i])
for i in range(mid, len(ans)):
    right+=int(ans[i])

#print(left, right)
if(left==right):
    print("LUCKY")
else:
    print("READY")