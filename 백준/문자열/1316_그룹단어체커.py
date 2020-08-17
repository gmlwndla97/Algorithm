import sys

sum = 0
n=int(sys.stdin.readline().rstrip())
for i in range(0,n):
    visit = [0] * 26

    str=sys.stdin.readline().rstrip()
    str=list(str)
    prev=str[0]
    visit[ord(prev)-97]=1
    flag=True
    if(len(str)==1):
        sum+=1
    else:
        for j in range(1, len(str)):
            if str[j]!=prev:
                if visit[ord(str[j])-97]==1:
                    #print(str[j])
                    break
            prev=str[j]
            visit[ord(prev)-97]=1
            if j==len(str)-1:
                sum+=1
print(sum)