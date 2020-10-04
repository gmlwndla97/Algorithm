import sys
ans=sys.stdin.readline().rstrip()
num=''
arr=[]
for i in range(0, len(ans)):
    #if(ans[i]!='0'):
        idx = (len(ans) - i) % 3
        if(ans[i]=='0'):
            arr.append((idx, 0))
        else:
            arr.append((idx, int(pow(2,idx))))

print(arr)
print(num)