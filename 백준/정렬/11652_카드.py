import sys
n=int(sys.stdin.readline().rstrip())
dic={}
for i in range(0, n):
    x=int(sys.stdin.readline().rstrip())
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1

dic=sorted(dic.items(), key=lambda x:(-x[1], x[0]))
#print(dic)
print(dic[0][0])
