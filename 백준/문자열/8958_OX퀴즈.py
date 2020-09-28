import sys
n=int(sys.stdin.readline().rstrip())


for i in range(0, n):
    ans=sys.stdin.readline().rstrip()
    idx = 0
    cnt = []
    for j in range(0, len(ans)):
        if ans[j]=='X':
            cnt.append(0)
            idx+=1
        elif ans[j]=='O':
            if j==0:
                cnt.append(1)
                idx+=1
            else:
                if cnt[idx-1]!=0:
                    prev=cnt[idx-1]
                    cnt.append(prev+1)
                    idx+=1
                else:
                    cnt.append(1)
                    idx+=1


    result = 0
    for i in cnt:
        result += i

    print(result)