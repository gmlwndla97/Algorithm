import sys
s=sys.stdin.readline().rstrip()
onecount=0
zerocount=0
if(s[0]=='0'):
    zerocount+=1
else:
    onecount+=1

for i in range(0, len(s)-1):
    if(s[i]!=s[i+1]):
        if(s[i]=='0'):
            onecount+=1
        else:
            zerocount+=1

print(min(onecount, zerocount))



